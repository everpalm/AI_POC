"""
This script retrieves the CPU information of the system and returns the CPU model name.

Usage:
    Run the script and it will print the CPU model name to the console.
"""

import platform

def get_cpu_model():
    """
    Gets the CPU model name from the system.
    
    Returns:
        str: The CPU model name.
    """
    # Retrieve CPU information using platform.uname()
    cpu_info = platform.uname()
    # Return the CPU model
    return cpu_info.processor

if __name__ == '__main__':
    # Print the CPU model name to the console
    cpu_model = get_cpu_model()
    print(f'CPU Model: {cpu_model}')