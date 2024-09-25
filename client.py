import socket

def send_dt_request(byte):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes([byte]), ('localhost', 9999))  # Send the byte
    
    # Wait for the response from the server
    response, addr = sock.recvfrom(1024)
    print("Received:", response.decode())

# In the user context, 0x01 switches to product context
send_dt_request(0x01)  # Switch to product context
send_dt_request(0x01)  # Request product name (Widget)

# In the product context, 0x01 switches to device_info context
send_dt_request(0x01)  # Switch to device_info context
send_dt_request(0x02)  # Request device status (Active)

# In the device_info context, 0x01 switches to control context
send_dt_request(0x01)  # Switch to control context
send_dt_request(0x01)  # Request to turn device ON (Device: ON)

