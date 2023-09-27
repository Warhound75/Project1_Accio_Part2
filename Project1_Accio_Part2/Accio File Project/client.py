import socket
import sys
import time
import random

# Constants for commands
ACCIO_COMMAND = b'accio\r\n'
BUFFER_SIZE = 1024

def main():
    if len(sys.argv) < 4:
        print("Usage: python client.py <SERVER_IP> <SERVER_PORT> <TEST_CASE>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    test_case = int(sys.argv[3])

    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_ip, server_port))

        # Send ACCIO_COMMAND
        client_socket.sendall(ACCIO_COMMAND)

        if test_case == 1:
            # Test case 1: Server receives a small amount of data (~500 bytes)
            data_to_send = b'x' * 500
        elif test_case == 2:
            # Test case 2: Server receives a large amount of data (~10 MiBytes)
            data_to_send = b'x' * 10000000
        elif test_case == 3:
            # Test case 3: Server receives a large amount of data with delays and errors
            data_to_send = b'x' * 10000000
            delay = random.uniform(0.5, 1.5)  # Random delay between 0.5 and 1.5 seconds
            time.sleep(delay)
            if random.random() < 0.2:  # Simulate 20% packet loss
                data_to_send = b''

        # Send the data
        client_socket.sendall(data_to_send)

        # Receive and print the response from the server
        response = client_socket.recv(BUFFER_SIZE)  # Adjust the buffer size as needed
        print("Server Response:", response.decode('utf-8'))  # Decode the response if it's in text format

    except socket.error as e:
        print("Socket error:", e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
