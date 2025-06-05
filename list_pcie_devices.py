"""
This module provides a function to list PCIe devices on the system.

Usage:
    Call the `list_pcie_devices` function to retrieve
a list of PCIe devices.
    Ensure you have the necessary permissions to access PCIe information.
"""

import subprocess


def list_pcie_devices():
    """
    Lists all PCIe devices on the system by executing the
    `lspci` command and parsing the output.

    Returns:
        List[dict]: A list of dictionaries containing information about each PCIe device.
    """
    devices = []  # Initialize an empty list to hold device information

    try:
        # Execute the lspci command to get the list of PCIe devices
        result = subprocess.run(['lspci', '-m'], capture_output=True, text=True, check=True)

        # Split the output into lines and process each line
        for line in result.stdout.strip().split('\n'):
            fields = line.split('\t')  # Split line by tab characters
            if len(fields) >= 7:
                # Create a dictionary for each device with relevant info
                device = {
                    'domain': fields[0],  # Domain of the device
                    'bus': fields[1],     # Bus ID
                    'slot': fields[2],    # Device and function
                    'vendor_id': fields[3],
                    'device_id': fields[4],
                    'vendor_name': fields[5],
                    'device_name': fields[6]  # Device description
                }
                devices.append(device)  # Add device to the list
    except subprocess.CalledProcessError as e:
        print(f'Error occurred while listing PCIe devices: {e}')  # Log any errors encountered
    return devices  # Return the list of devices.