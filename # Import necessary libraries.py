# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm

# Define the file path to the Excel file
file_path = "C:/Users/raymo/Downloads/baseball.xlsx"

# Read the Excel file into a DataFrame
try:
    data = pd.read_excel(file_path)
except FileNotFoundError:
    print("File not found. Please ensure the file path is correct.")
    exit()

# Display the first few rows of the DataFrame to understand its structure
print("First few rows of the data:")
print(data.head())

# Extract the required features and target variable from the DataFrame
# Features: Runs Scored, Runs Allowed, Wins, On-base percentage (OBP), Slugging percentage (SLG), Team Batting Average
features = data[['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']]
target = data['Playoffs']  # Target variable: Playoffs (1 for made playoffs, 0 for did not)

# Initialize the logistic regression model
model = LogisticRegression()

# Train the model using all the data
model.fit(features, target)

# Get the coefficients and intercept of the model
coefficients = model.coef_
intercept = model.intercept_

# Print the regression statistics
print("\nRegression statistics:")
print("Coefficients:", coefficients)
print("Intercept:", intercept)

# Fit a logistic regression model using statsmodels for more detailed statistics
X_with_intercept = sm.add_constant(features)  # Add intercept term
logit_model = sm.Logit(target, X_with_intercept)
result = logit_model.fit()

# Print detailed regression summary
print("\nDetailed regression summary:")
print(result.summary())
