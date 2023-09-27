import socket
import sys
import signal
import time
import threading
import random

# Constants for commands
ACCIO_COMMAND = b'accio\r\n'

# Global variable to control signal handling
not_stopped = True

# Signal handler function
def signal_handler(signum, frame):
    global not_stopped
    not_stopped = False

# Function to handle an individual connection
def handle_connection(client_socket):
    # Send ACCIO_COMMAND
    client_socket.send(ACCIO_COMMAND)

    # Receive confirmation for ACCIO_COMMAND
    confirmation = client_socket.recv(len(ACCIO_COMMAND))
    if confirmation != ACCIO_COMMAND:
        print("ERROR: Invalid confirmation for ACCIO_COMMAND")
        return

    # Receive and count the binary file data with emulated delays and errors
    start_time = time.time()
    bytes_received = 0
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        bytes_received += len(data)

        # Simulate random transmission errors (5% probability)
        if random.random() < 0.05:
            print("ERROR: Transmission error occurred")
            break

        # Simulate random delays (1-2 seconds)
        time.sleep(random.uniform(1, 2))

        # Reset the timeout timer since data is received
        start_time = time.time()

    # Calculate the time elapsed during reception
    elapsed_time = time.time() - start_time

    # If no data received for more than 10 seconds, abort the connection
    if elapsed_time > 10:
        print("ERROR: Connection timed out (no data received)")
    else:
        print("Number of bytes received:", bytes_received)

    # Close the client socket
    client_socket.close()

def start_server(port):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified port on all interfaces
    server_socket.bind(('0.0.0.0', port))

    # Listen for incoming connections (parameter set to 10 to handle up to 10 simultaneous connections)
    server_socket.listen(10)
    print("Server listening on port", port)

    # Register signal handlers for graceful termination
    signal.signal(signal.SIGINT, signal_handler)

    while not_stopped:
        try:
            # Accept incoming connections
            client_socket, addr = server_socket.accept()
            print("Accepted connection from", addr)

            # Handle the connection in a separate thread
            client_thread = threading.Thread(target=handle_connection, args=(client_socket,))
            client_thread.start()

        except KeyboardInterrupt:
            pass  # Handle keyboard interrupt gracefully

    # Close the server socket before exiting
    server_socket.close()
