"""
Data Processing Script

This script is designed to process a dataset by performing basic operations such as loading,
cleaning, and summarizing the data. It is intended for use in data analysis workflows.

Usage:
1. Ensure the dataset is in CSV format and placed in the same directory as this script.
2. Run the script to load and process the data.
"""

import pandas as pd  # Import pandas library for data manipulation

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)  # Load CSV data into a DataFrame

def clean_data(df):
    """Clean the dataset by handling missing values and duplicates."""
    df = df.dropna()  # Remove rows with missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    return df

def summarize_data(df):
    """Return a summary of the dataset."""
    return df.describe()  # Return descriptive statistics of the DataFrame

if __name__ == '__main__':
    # Main execution flow
    data_file = 'data.csv'  # Specify the filename of the dataset
    data = load_data(data_file)  # Load the data
    cleaned_data = clean_data(data)  # Clean the data
    summary = summarize_data(cleaned_data)  # Summarize the cleaned data
    print(summary)  # Output the summary to the console