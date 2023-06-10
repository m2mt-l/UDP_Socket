import socket, os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = "./udp_socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"starting up on {server_address}")
sock.bind(server_address)

while True:
    print("\nwaiting to receive messages")
    data, address = sock.recvfrom(4096)

    print(f"received {len(data)} bytes from {address}")
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print(f"sent {sent} bytes back to {address}")
