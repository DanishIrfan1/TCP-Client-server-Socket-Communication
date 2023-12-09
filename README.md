# Simple Python TCP Client-Server Example

This is a basic example of a TCP client-server communication implemented in Python.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python (version 3.x recommended)

## Major Concepts

- **Socket Programming:** The communication between the client and server is established using Python's `socket` module.

- **TCP (Transmission Control Protocol):** The program uses TCP for reliable communication between the client and server.

## How to Run

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:DanishIrfan1/TCP-Client-server-Socket-Communication.git
    ```
2. Navigate to the directory containing the code:
3. Open two terminal windows, one for the server and one for the client.
4. Run the server code:

   ```bash
   python server.py
   ```
5. Run the client code:

   ```bash
    python client.py
    ```

The client will connect to the server, exchange messages, and then disconnect.