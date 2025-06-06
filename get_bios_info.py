"""
This script retrieves the BIOS version information
from the system running on a Linux (Ubuntu) platform.

Usage:
    Run this script in a terminal to display the BIOS version.
"""

import subprocess  # Import subprocess to execute shell commands

def get_bios_version():
    """Fetch and return the BIOS version as a string."""
    try:
        # Execute the command to get BIOS information
        bios_info = subprocess.check_output("sudo dmidecode -s bios-version", shell=True, text=True)
        return bios_info.strip()  # Remove any surrounding whitespace
    except subprocess.CalledProcessError as e:
        # Handle errors in command execution
        return f"Error fetching BIOS information: {e}"

if __name__ == "__main__":
    # Main execution point
    bios_version = get_bios_version()
    print(f"BIOS Version: {bios_version}")  # Print the BIOS version