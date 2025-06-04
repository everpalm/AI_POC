"""
Data Analysis Tool

This script provides functionality for basic data analysis on numeric datasets.
It includes methods for calculating the mean, median, and mode of a dataset.

Usage:
1. Import the module
2. Create a DataAnalysis instance with your dataset
3. Call the desired methods to perform analysis
"""

from collections import Counter
import numpy as np

class DataAnalysis:
    def __init__(self, data):
        """
        Initializes the DataAnalysis object with the dataset.

        Args:
            data (list or np.array): A collection of numeric values.
        """
        self.data = np.array(data)  # Convert input to a numpy array for easier manipulation

    def mean(self):
        """
        Calculate and return the mean of the dataset.

        Returns:
            float: The mean value of the dataset.
        """
        return np.mean(self.data)  # Use numpy's mean function to calculate

    def median(self):
        """
        Calculate and return the median of the dataset.

        Returns:
            float: The median value of the dataset.
        """
        return np.median(self.data)  # Use numpy's median function to calculate

    def mode(self):
        """
        Calculate and return the mode of the dataset.

        Returns:
            float: The mode value of the dataset (most common value).
        """
        data_count = Counter(self.data)  # Count the frequency of each value
        mode_data = data_count.most_common(1)  # Get the most common value
        return mode_data[0][0] if mode_data else None  # Return the mode or None if no mode

# Example usage (this part would not be included in the final script):
# if __name__ == '__main__':
#     data = [1, 2, 2, 3, 4]
#     analysis = DataAnalysis(data)
#     print("Mean:", analysis.mean())
#     print("Median:", analysis.median())
#     print("Mode:", analysis.mode())
