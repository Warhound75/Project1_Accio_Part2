# Accio File Transfer Project

This is a multi-part project that involves implementing a simple client-server application for transferring files over a TCP connection. The project is divided into three parts, each building on the previous one.

The project consists of the following components:

- `client.py`: Python script for the Accio client.(Part 1)
- `server-s.py`: Python script for the simplified Accio server (Part 2).
- `server.py`: Python script for the final Accio server (Part 3).
- `server_module.py`: Module containing server-related functions.
- `README.md`: This documentation file.

## Part 1: Accio Client

### Problems Encountered and Solutions

Issue 1: Understanding the requirements and specifications.
Solution: Carefully read the project description, and create a checklist of requirements for Part 1.

Issue 2: Establishing a connection to the server.
Solution: Implemented a client using Python and BSD sockets. Created a socket, established a connection to the server, and sent a file.

Issue 3: Ensuring that the client works with binary data and does not use 'utf-8' encoding.
 Solution: Write code to work directly with binary data and used byte strings (e.g., `b"accio\r\n"`) instead of encoding/decoding with 'utf-8'.

### Acknowledgments

- I referred to the official Python documentation for socket programming to understand socket operations and methods.

## Part 2: Accio Server Simplified

### Problems Encountered and Solutions (Continued)

Issue 4: Implementing the server to handle connections and signals.
 Solution: Created a server that gracefully handles signals (SIGINT) for termination and accepts client connections.

Issue 5: Sending and receiving commands and data.
 Solution: Implemented code to send the 'accio\r\n' command and receive data from the client.

Issue 6: Handling multiple sequential connections.
Solution: Used multi-threading to handle multiple connections sequentially without rejecting new connections.

Issue 7: Implementing a timeout mechanism.
Solution: Added code to track the time elapsed and abort the connection if no data is received for more than 10 seconds.

### Acknowledgments

I referred to online resources and tutorials on socket programming in Python to better understand how to handle multiple connections and signals.

## Part 3: Accio Server

### Problems Encountered and Solutions (Continued)

Issue 8: Extending the server to the complete file transfer application.
Solution: Implemented a complete server that can handle large files and various testing scenarios.

Issue 9: Testing the server for various scenarios.
Solution: Conducted extensive testing using the instructor's version of the client, including both small and large data transfers with and without emulated delays and transmission errors.

### Acknowledgments

- I would like to acknowledge the online Python socket programming community for sharing valuable insights and code examples that helped me in implementing various server functionalities.

---

## How to Use

To run the Accio project, follow these steps:

1. Start the server:
   - For Part 2: Use `python3 server-s.py <PORT>` to start the simplified server.
   - For Part 3: Use `python3 server.py <PORT>` to start the final server.

2. Start the client:
   - Use `python3 client.py <SERVER_IP> <SERVER_PORT>` to start the client and connect to the server.
