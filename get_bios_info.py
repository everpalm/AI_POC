"""
This script retrieves the BIOS information of the system and returns it as output.

Usage:
    Run the script in a Python environment. It will print the BIOS information.
"""

import subprocess


def get_bios_info():
    """
    Retrieves BIOS information using the 'wmic' command on Windows or 'dmidecode' on Linux.
    Returns BIOS information as a dictionary.
    """  
    bios_info = {}
    
    try:
        # Check the operating system
        if subprocess.os.name == 'nt':  # Windows
            # Execute the command to get BIOS information
            output = subprocess.check_output(['wmic', 'bios', 'get', '/format:list'])
            output = output.decode('utf-8')
            # Parse the output into a dictionary
            for line in output.splitlines():
                if '=' in line:
                    key, value = line.split('=', 1)
                    bios_info[key.strip()] = value.strip()
        else:  # Assume Linux
            # Execute the command to get BIOS information
            output = subprocess.check_output(['sudo', 'dmidecode', '-t', '0'])
            output = output.decode('utf-8')
            # Process the output to extract BIOS information
            bios_info['BIOS'] = output

    except subprocess.CalledProcessError as e:
        print(f'Error retrieving BIOS information: {e}')
        return None

    return bios_info


if __name__ == '__main__':
    bios_info = get_bios_info()
    if bios_info:
        print(bios_info)  # Print the BIOS information