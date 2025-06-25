"""
Get CPU information from a Linux (Ubuntu) platform.

This module provides a function to retrieve the BIOS version of the CPU.
"""

import subprocess


def get_cpu_info():
    """
    Retrieve the BIOS version from the system information.
    
    Returns:
        str: BIOS version of the CPU.
    """
    try:
        # Use the `dmidecode` command to get BIOS information
        result = subprocess.run(['sudo', 'dmidecode', '-t', 'bios'],
                                capture_output=True,
                                text=True,
                                check=True)

        # Find the line that contains the BIOS version
        for line in result.stdout.splitlines():
            if 'Version' in line:
                return line.split(':')[1].strip()  # Return the version after ':'

    except subprocess.CalledProcessError as e:
        return f"Error retrieving CPU info: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# If the script is run directly, print the BIOS version
if __name__ == '__main__':
    print(get_cpu_info())