"""
This script retrieves and displays information about the CPU.

Usage:
    python get_cpu_info.py
"""

import psutil  # Importing the psutil library to access system information


def get_cpu_info():
    """
    Get detailed CPU information.

    Returns:
        dict: A dictionary containing CPU information like number of cores,
              frequency, and utilization.
    """
    # Fetching the number of logical CPUs
    cpu_count = psutil.cpu_count(logical=True)
    # Fetching the CPU frequencies
    cpu_freq = psutil.cpu_freq()._asdict()  # Getting frequency details as a dictionary
    # Fetching CPU utilization percentage
    cpu_utilization = psutil.cpu_percent(interval=1)  # Getting utilization with a one second interval

    # Compiling the info into a dictionary
    cpu_info = {
        'Logical CPUs': cpu_count,
        'Frequency (MHz)': cpu_freq,
        'CPU Utilization (%)': cpu_utilization
    }

    return cpu_info


def display_cpu_info(info):
    """
    Display the CPU information in a readable format.

    Args:
        info (dict): The dictionary containing CPU information.
    """
    print("CPU Information:")
    print(f"Logical CPUs: {info['Logical CPUs']}")
    print(f"Frequency (MHz): {info['Frequency (MHz)']['current']} (Min: {info['Frequency (MHz)']['min']}, Max: {info['Frequency (MHz)']['max']})")
    print(f"CPU Utilization (%): {info['CPU Utilization (%)']}\n")


if __name__ == '__main__':  # Ensuring code runs as a standalone script
    cpu_info = get_cpu_info()  # Get the CPU information
    display_cpu_info(cpu_info)  # Display the information