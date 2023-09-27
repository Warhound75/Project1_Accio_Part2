import socket
import sys
import threading
import time
import signal
import random

# Constants
ACCIO_COMMAND = b'accio\r\n'
BUFFER_SIZE = 1024
MAX_CONNECTIONS = 10

# Global flag for signal handling
not_stopped = True

def signal_handler(signum, frame):
    global not_stopped
    print("Received signal {}. Exiting gracefully.".format(signum))
    not_stopped = False

def handle_client(client_socket):
    try:
        # Send ACCIO_COMMAND
        client_socket.sendall(ACCIO_COMMAND)

        # Set a timeout for receiving data (10 seconds)
        client_socket.settimeout(10)

        # Receive and count data
        total_bytes_received = 0
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            total_bytes_received += len(data)

        if total_bytes_received == 0:
            print("Connection timed out. Printing ERROR.")
            client_socket.sendall(b'ERROR')
        else:
            print("Received {} bytes".format(total_bytes_received))

    except socket.timeout:
        print("Connection timed out. Printing ERROR.")
        client_socket.sendall(b'ERROR')
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the client socket
        client_socket.close()

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("ERROR: Usage: python server.py <PORT>\n")
        sys.exit(1)

    try:
        port = int(sys.argv[1])

        # Create a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind to all available network interfaces
        server_socket.bind(('0.0.0.0', port))

        # Start listening for incoming connections
        server_socket.listen(MAX_CONNECTIONS)

        # Set up signal handlers
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGQUIT, signal_handler)

        while not_stopped:
            print("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

    except ValueError:
        sys.stderr.write("ERROR: Invalid port number\n")
        sys.exit(1)
    except socket.error as e:
        sys.stderr.write("ERROR: Socket error - {}\n".format(e))
    except Exception as e:
        sys.stderr.write("ERROR: An error occurred - {}\n".format(e))
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
