import socket

UDP_IP = "0.0.0.0" # ip to listen at, zeroes means all addresses
#UDP_IP = "192.168.2.51"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP Server listening on {UDP_IP}:{UDP_PORT}")

while True:
    try:
        print("beep")
        data, addr = sock.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")
    except Exception as e:
        print(f"Error receiving message: {e}")
