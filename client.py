import socket

def send_dt_request(byte):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes([byte]), ('localhost', 9999))  # Send the byte
    
    # Wait for the response from the server
    response, addr = sock.recvfrom(1024)
    print("Received:", response.decode())

# Example usage: Chain of actions
# 1. Start in the 'user' context and request the user name
send_dt_request(0x01)  # Request user name (Alice)

# 2. Switch to 'product' context and request the product price
send_dt_request(0x02)  # Switch to product context
send_dt_request(0x02)  # Request product price (Price: $19.99)

# 3. Switch to 'device_info' context and request device status
send_dt_request(0x03)  # Switch to device_info context
send_dt_request(0x02)  # Request device status (Device Status: Active)

# 4. Switch to 'control' context and turn the device on, then off
send_dt_request(0x04)  # Switch to control context
send_dt_request(0x01)  # Turn device on (Device: ON)
send_dt_request(0x02)  # Turn device off (Device: OFF)

# 5. Switch back to 'user' context
send_dt_request(0x01)  # Switch back to user context
