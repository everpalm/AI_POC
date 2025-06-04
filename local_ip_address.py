"""
This script retrieves and displays the local IP address of the
machine it is run on. It uses the built-in socket library to
obtain the IP address.

Usage:
1. Run the script.
2. The local IP address will be printed to the console.
"""

import socket  # Importing the socket library to interact with networking


def get_local_ip():
    """Retrieve the local IP address of the machine."""
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server (Google DNS) to get the local IP
        s.connect(('8.8.8.8', 80))  # DNS of Google
        local_ip = s.getsockname()[0]  # Get the IP address
    finally:
        s.close()  # Close the socket

    return local_ip


def main():
    """Main function to display the local IP address."""
    ip_address = get_local_ip()  # Call the function to get local IP
    print(f'Local IP address: {ip_address}')  # Print the IP address


if __name__ == '__main__':
    main()