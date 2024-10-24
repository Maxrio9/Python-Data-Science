# Subscriber Pipeline Starter Kit

This project contains a data pipeline for processing and analyzing subscriber data. It includes scripts for cleaning data, creating analytics-ready databases, and running automated tests.

## Folder Structure

subscriber-pipeline-starter-kit/
│
├── dev/
│ ├── production/
│ ├── script.py
│ ├── update_and_deploy.sh
│ ├── cademycode.db
│ ├── analytics_ready.db
│ ├── analytics_ready.csv
│ ├── changelog.txt
│ ├── error_log.txt
│ └── bash_script.log
│
└── README.md


- `dev/`: Main development directory
  - `production/`: Directory for production-ready files
  - `script.py`: Main Python script for data processing
  - `update_and_deploy.sh`: Bash script for running updates and deploying
  - `cademycode.db`: Input database
  - `analytics_ready.db`: Output analytics-ready database
  - `analytics_ready.csv`: CSV export of analytics-ready data
  - `changelog.txt`: Log of database updates
  - `error_log.txt`: Log of errors during script execution
  - `bash_script.log`: Log of bash script execution

## Running the Update Process

To run the update process and deploy the latest changes:

1. Ensure you have Bash installed on your system. If you're using Windows, you can use Git Bash.

2. Open a terminal or Git Bash.

3. Navigate to the `dev` directory:
   ```
   cd path/to/subscriber-pipeline-starter-kit/dev
   ```

4. Make sure the bash script is executable:
   ```
   chmod +x update_and_deploy.sh
   ```

5. Run the bash script:
   ```
   ./update_and_deploy.sh
   ```

6. The script will:
   - Run the Python script to process the data
   - Check for any updates in the database
   - If updates are found, move the new files to the production directory
   - Run unit tests to ensure everything is working correctly

7. Check the log files (`changelog.txt`, `error_log.txt`, and `bash_script.log`) for any issues or to confirm successful execution.

## Requirements

- Python 3.x
- Pandas
- SQLite3
- Bash (Git Bash for Windows users)

Make sure all required Python packages are installed before running the update process.

## Troubleshooting

If you encounter any issues:

1. Check the `error_log.txt` for Python script errors.
2. Check the `bash_script.log` for bash script execution logs.
3. Ensure all file paths in the scripts are correct for your system.
4. Verify that you have the necessary permissions to read/write in the project directories.

For any persistent issues, please contact the development team.