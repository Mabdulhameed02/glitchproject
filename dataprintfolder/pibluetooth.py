import bluetooth
import sqlite3

# Function to insert request data into the database
def insert_into_db(info):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("INSERT INTO requests (info) VALUES (?)", (info,))
    conn.commit()
    conn.close()

# Bluetooth server function
def bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Bind to port 1
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]

    # Advertise the Bluetooth service
    bluetooth.advertise_service(
        server_socket,
        "RaspberryPiServer",
        service_id=bluetooth.SERIAL_PORT_CLASS,
        service_classes=[bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE]
    )

    print(f"Waiting for Bluetooth connection on RFCOMM channel {port}...")

    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")

    try:
        while True:
            # Receive data (info) from the mobile app
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            print(f"Received: {data}")

            # Insert the received info into the database
            insert_into_db(data)

            # Send a confirmation message back to the mobile app
            client_socket.send("Data received and stored".encode("utf-8"))

    except OSError:
        pass

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    bluetooth_server()
