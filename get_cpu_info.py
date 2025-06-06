"""
Get CPU information from a Linux (Ubuntu) platform.

This script retrieves and returns the BIOS version of the CPU.
"""

import subprocess


def get_cpu_info():
    """Fetch the BIOS version from the system using the `dmidecode` command."""
    try:
        # Execute the command to retrieve BIOS information
        result = subprocess.run(['sudo', 'dmidecode', '-s', 'bios-version'],
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE,
                                check=True,
                                text=True)

        # Return the BIOS version from the command output
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Handle errors in command execution
        return f"Error retrieving BIOS version: {e.stderr.strip()}"

# Example usage:
# if __name__ == '__main__':
#     print(get_cpu_info())