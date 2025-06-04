"""
This script lists all PCIe devices on a Linux Ubuntu system using the lspci command.

Usage:
    Run the script in a terminal. It will output the list of PCIe devices.
"""

import os


def list_pcie_devices():
    """
    Executes the lspci command and retrieves the list of PCIe devices.
    
    Returns:
        str: A string containing the list of PCIe devices.
    """
    devices = os.popen("lspci").read()  # Execute lspci command and read output
    return devices  # Return the output of the command


if __name__ == "__main__":
    pcie_devices = list_pcie_devices()  # Get the PCIe devices
    print("PCIe Devices:\n", pcie_devices)  # Print the list of PCIe devices