# Import necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import zscore

# Load the dataset
file_path = '/content/First_Gulf_Bank_Dataset.csv'
dataframe = pd.read_csv(file_path)

# Z-score method to identify outliers
z_scores = np.abs(zscore(dataframe.select_dtypes(include=[np.number])))

# Define the threshold for outliers (typically 3 or more standard deviations from the mean)
threshold = 3

# Identify outliers
outliers = (z_scores > threshold)

# Create a summary of the number of outliers for each column
outliers_summary = {}
for column in dataframe.select_dtypes(include=[np.number]).columns:
    outliers_summary[column] = np.sum(outliers[column])

# Print the summary of outliers in each numerical column
print(outliers_summary)
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean_preprocess_feature_engineer(file_path):
    # Load the dataset
    dataframe = pd.read_csv(file_path)

    # 1. Preprocessing: Handle categorical variables
    # Label Encoding for binary categorical columns
    binary_cols = ['GENDER', 'OCCUPATION', 'ACC_TYPE']  # Replace with actual binary columns in the dataset
    label_encoders = {}
    for col in binary_cols:
        le = LabelEncoder()
        dataframe[col] = le.fit_transform(dataframe[col])
        label_encoders[col] = le  # Store encoders for potential inverse_transform later

    # 2. Feature Engineering: Create new features
    # Calculate the ratio of having a credit card by gender
    gender_cc_ratio = dataframe.groupby('GENDER')['FLG_HAS_CC'].mean()  # Proportion of customers with CC in each gender
    # Map this ratio back to the original dataframe
    dataframe['GENDER_CC_RATIO'] = dataframe['GENDER'].map(gender_cc_ratio)

    # 3. Convert 'BALANCE' to a numerical category (as integers)
    balance_bins = [0, 1000, 5000, 10000, np.inf]  # Define your bins
    balance_labels = [0, 1, 2, 3]  # Corresponding numerical labels for categories
    dataframe['BALANCE_CATEGORY'] = pd.cut(dataframe['BALANCE'], bins=balance_bins, labels=balance_labels, right=False)

    # Optionally drop the original 'BALANCE' column if not needed
    # dataframe.drop(columns=['BALANCE'], inplace=True)

    return dataframe, label_encoders

# Specify the path to your CSV file here
file_path = '/content/First_Gulf_Bank_Dataset.csv'  # Replace this with the actual path to your CSV file

# Usage
cleaned_data, label_encoders = clean_preprocess_feature_engineer(file_path)

# Display the first few rows of the processed dataframe
print(cleaned_data.head())
from sklearn.model_selection import train_test_split #importing libaray from sklearn
#x = cleaned_data.drop(columns=['FLG_HAS_CC', 'CUST_ID', 'TARGET','ACC_OP_DATE'],axis=1) # Takes other variables other than FLG_HAS_CC
x= cleaned_data[['HOLDING_PERIOD']] # Takes other variables other than FLG_HAS_CC
y = cleaned_data[['FLG_HAS_CC']] # takes FLG_HAS_CC

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # Splits the data into training and test sets.
print(y_test)