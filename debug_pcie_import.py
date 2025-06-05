"""
This script attempts to import the function 'get_pcie_devices'
from the module 'list_pcie_devices'. If the import fails,
it will handle the ImportError and inform the user.

Usage:
    Run this script to check and demonstrate the import functionality.
"""

try:
    # Attempting to import the get_pcie_devices function
    from list_pcie_devices import get_pcie_devices
    print("Import successful! You can now use 'get_pcie_devices'.")
except ImportError as e:
    # Handling the ImportError if the function does not exist
    print(f"ImportError: {e}")
    print("Please check if 'get_pcie_devices' is defined in 'list_pcie_devices'.")
    print("If it is not, make sure the module is correctly implemented and available.")