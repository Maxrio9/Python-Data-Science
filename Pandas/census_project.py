# Data Shape
# column	description
# first_name	The respondent’s first name.
# last_name	The respondent’s last name.
# birth_year	The respondent’s year of birth.
# voted	If the respondent participated in the current voting cycle.
# num_children	The number of children the respondent has.
# income_year	The average yearly income the respondent earns.
# higher_tax	The respondent’s answer to the question: “Rate your agreement with the statement: the wealthy should pay higher taxes.”
# marital_status	The respondent’s current marital status.

import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

census.birth_year = census.birth_year.replace("missing", "1967")
census.birth_year = census.birth_year.astype("int")
census.higher_tax = pd.Categorical(census.higher_tax, ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"], ordered=True)
census.higher_tax = census.higher_tax.cat.codes
census = pd.get_dummies(census, columns=['marital_status'])

print(census.head())
print(census.dtypes)

print(census.higher_tax.unique())
print("Average birth year:", census.birth_year.mean())
print("Average Higher Tax for the Rich:", census.higher_tax.mean())

# Create a new variable called age_group, which groups respondents based on their birth year.
# The groups should be in five-year increments, e.g., 25-30, 31-35, etc. Then label encode
# the age_group variable to assist the Census team in the event they would like to use machine
# learning to predict if a respondent thinks the wealthy should pay higher taxes based on their
# age group.