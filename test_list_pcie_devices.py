import pytest
from list_pcie_devices import get_pcie_devices


def test_get_pcie_devices():
    """
    Test the get_pcie_devices function from list_pcie_devices.
    This will validate that the function returns a list of PCIe devices
    with the expected format and content.
    """
    # Call the function to get the list of PCIe devices
    devices = get_pcie_devices()
    
    # Validate that the response is a list
    assert isinstance(devices, list), "Expected a list of devices"
    
    # Assuming each device should be a dictionary with specific keys
    expected_keys = {'name', 'vendor', 'device_id'}
    for device in devices:
        # Check if each device is a dictionary
        assert isinstance(device, dict), "Each device should be a dictionary"
        # Check that each device has the correct keys
        assert expected_keys.issubset(device.keys()), \
            f"Device {device} missing expected keys"

    # Additional tests can be added here for more specific validations