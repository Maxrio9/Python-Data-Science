import sqlite3
import pandas as pd
import numpy as np
from contextlib import closing
import unittest
import logging
import os
import time
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up error log
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('error_log.txt')
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
error_logger.addHandler(error_handler)

# Set up changelog
changelog_logger = logging.getLogger('changelog_logger')
changelog_logger.setLevel(logging.INFO)
changelog_handler = logging.FileHandler('changelog.txt')
changelog_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
changelog_logger.addHandler(changelog_handler)

def load_and_clean_database(db_file='cademycode.db'):
    try:
        # Establish a connection to the database
        with closing(sqlite3.connect(db_file)) as conn:
            # Get list of all tables
            tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
            
            # Dictionary to store DataFrames
            dataframes = {}
            
            for table_name in tables['name']:
                # Read each table into a DataFrame
                df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                print(f"\nInspecting table: {table_name}")
                
                # Basic info and missing data check
                print(df.info())
                print("\nMissing values:")
                print(df.isnull().sum())
                
                # Check for duplicate rows
                duplicates = df.duplicated().sum()
                print(f"\nNumber of duplicate rows: {duplicates}")
                
                # Basic cleaning operations
                # 1. Remove duplicate rows
                df = df.drop_duplicates()
                
                # 2. Handle missing values (example: fill numeric with median, categorical with mode)
                for column in df.columns:
                    if df[column].dtype in ['int64', 'float64']:
                        df[column].fillna(df[column].median(), inplace=True)
                    else:
                        df[column].fillna(df[column].mode()[0], inplace=True)
                
                # 3. Convert date columns to datetime (assuming 'date' is in column name)
                date_columns = [col for col in df.columns if 'date' in col.lower()]
                for date_col in date_columns:
                    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
                
                # 4. Remove any rows with invalid data (example: future dates)
                if date_columns:
                    df = df[df[date_columns[0]] <= pd.Timestamp.now()]
                
                # Store the cleaned DataFrame
                dataframes[table_name] = df
                
                print(f"\nCleaned data for {table_name}:")
                print(df.info())
            
            return dataframes
    
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# Call the function to load and clean the database
cleaned_data = load_and_clean_database()

def create_analytics_ready_data(cleaned_data, output_db='analytics_ready.db', output_csv='analytics_ready.csv'):
    if not cleaned_data:
        print("No cleaned data available.")
        return

    # Create a new SQLite database for analytics-ready data
    with closing(sqlite3.connect(output_db)) as conn:
        for table_name, df in cleaned_data.items():
            # Write each DataFrame to the new database
            df.to_sql(table_name, conn, index=False, if_exists='replace')
        
        print(f"Analytics-ready database created: {output_db}")
    
    # Prepare a single DataFrame for CSV export
    main_df = None
    for table_name, df in cleaned_data.items():
        if main_df is None:
            main_df = df
        else:
            # Attempt to merge DataFrames based on common columns
            common_columns = list(set(main_df.columns) & set(df.columns))
            if common_columns:
                # Convert common columns to the same type before merging
                for col in common_columns:
                    if main_df[col].dtype != df[col].dtype:
                        # Convert both to string as a safe option
                        main_df[col] = main_df[col].astype(str)
                        df[col] = df[col].astype(str)
                
                main_df = pd.merge(main_df, df, on=common_columns, how='outer', suffixes=(f'_{table_name}', ''))
            else:
                # If no common columns, add a unique identifier and perform a cross join
                main_df['key'] = 1
                df['key'] = 1
                main_df = pd.merge(main_df, df, on='key', how='outer', suffixes=(f'_{table_name}', ''))
                main_df.drop('key', axis=1, inplace=True)
    
    # Export to CSV
    if main_df is not None:
        main_df.to_csv(output_csv, index=False)
        print(f"Analytics-ready CSV file created: {output_csv}")
    else:
        print("No data to export to CSV.")

# Create analytics-ready database and CSV
create_analytics_ready_data(cleaned_data)

# Verify the contents of the new database
def verify_analytics_database(db_file='analytics_ready.db'):
    try:
        with closing(sqlite3.connect(db_file)) as conn:
            # Get list of all tables
            tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
            
            for table_name in tables['name']:
                # Read each table into a DataFrame
                df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                print(f"\nTable: {table_name}")
                print(df.info())
                print(df.head())
    
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")

# Verify the new database
verify_analytics_database()

def check_for_updates(input_db='cademycode.db', output_db='analytics_ready.db'):
    input_mod_time = os.path.getmtime(input_db)
    output_mod_time = os.path.getmtime(output_db) if os.path.exists(output_db) else 0
    
    return input_mod_time > output_mod_time

def update_database():
    if check_for_updates():
        logger.info("Updates detected. Processing new data...")
        cleaned_data = load_and_clean_database()
        create_analytics_ready_data(cleaned_data)
        changelog_logger.info("Database updated successfully.")
    else:
        logger.info("No updates required.")

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Create a test database
        self.test_db = 'test_cademycode.db'
        conn = sqlite3.connect(self.test_db)
        c = conn.cursor()
        c.execute('''CREATE TABLE test_table
                     (id INTEGER PRIMARY KEY, name TEXT, value REAL)''')
        c.execute("INSERT INTO test_table VALUES (1, 'Test', 10.5)")
        conn.commit()
        conn.close()

    def tearDown(self):
        # Remove the test database
        os.remove(self.test_db)

    def test_load_and_clean_database(self):
        cleaned_data = load_and_clean_database(self.test_db)
        self.assertIsNotNone(cleaned_data)
        self.assertIn('test_table', cleaned_data)
        self.assertEqual(len(cleaned_data['test_table']), 1)

    def test_create_analytics_ready_data(self):
        cleaned_data = load_and_clean_database(self.test_db)
        create_analytics_ready_data(cleaned_data, 'test_analytics_ready.db', 'test_analytics_ready.csv')
        self.assertTrue(os.path.exists('test_analytics_ready.db'))
        self.assertTrue(os.path.exists('test_analytics_ready.csv'))
        os.remove('test_analytics_ready.db')
        os.remove('test_analytics_ready.csv')

    def test_check_for_updates(self):
        # Create a dummy output database
        with open('dummy_output.db', 'w') as f:
            f.write('dummy')
        
        # Ensure the input database is "newer"
        os.utime(self.test_db, (datetime.now().timestamp(), datetime.now().timestamp()))
        
        self.assertTrue(check_for_updates(self.test_db, 'dummy_output.db'))
        os.remove('dummy_output.db')

def run_tests_and_update():
    try:
        # Run the update process
        update_database()
        
        # Run the unit tests
        suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseOperations)
        runner = unittest.TextTestRunner(verbosity=2)
        test_results = runner.run(suite)
        
        # Log test results
        if test_results.wasSuccessful():
            logger.info("All tests passed successfully.")
        else:
            error_logger.error("Some tests failed. Check the output for details.")
        
    except Exception as e:
        error_logger.error(f"An error occurred: {str(e)}")

# Run the tests and update process
run_tests_and_update()