"""
This script fetches CPU information using the psutil library.

Usage:
    Run the script to get details about the CPU, including the number of cores,
    maximum frequency, and current frequency.
"""

import psutil  # Import the psutil library to access system and hardware information

def get_cpu_info():
    """
    Returns a dictionary containing CPU information.
    """  
    cpu_info = {}  # Dictionary to hold CPU information
    cpu_info['logical_cores'] = psutil.cpu_count(logical=True)  # Get logical core count
    cpu_info['physical_cores'] = psutil.cpu_count(logical=False)  # Get physical core count
    cpu_info['max_frequency'] = psutil.cpu_freq().max  # Get max frequency of the CPU
    cpu_info['current_frequency'] = psutil.cpu_freq().current  # Get current frequency of the CPU

    return cpu_info  # Return the gathered CPU information

if __name__ == '__main__':  # Entry point of the script
    info = get_cpu_info()  # Fetch the CPU information
    print(info)  # Print the CPU information