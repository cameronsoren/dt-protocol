import socket

# Define byte-to-response maps for each context
context_maps = {
    'user': {
        0x01: 'User: Alice',
        0x02: 'Email: alice@example.com'
    },
    'product': {
        0x01: 'Product: Widget',
        0x02: 'Price: $19.99'
    },
    'device_info': {
        0x01: 'Device Model: X100',
        0x02: 'Device Status: Active'
    },
    'control': {
        0x01: 'Device: ON',
        0x02: 'Device: OFF'
    }
}

# Define consistent context-switch bytes
context_switch_map = {
    0x01: 'user',
    0x02: 'product',
    0x03: 'device_info',
    0x04: 'control'
}

# Function to check and switch contexts based on the byte received
def check_for_context_switch(byte_value):
    if byte_value in context_switch_map:
        return context_switch_map[byte_value]
    return None

def start_dt_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 9999))

    print("DT Protocol Server is running...")

    current_context = 'user'  # Default context

    while True:
        data, addr = sock.recvfrom(1)  # Receive 1 byte
        byte_value = data[0]

        # Check if the byte should switch context
        new_context = check_for_context_switch(byte_value)

        if new_context:
            current_context = new_context
            response = f"Switched to {current_context} context"
        else:
            # Fetch the appropriate response based on the current context
            response = context_maps[current_context].get(byte_value, 'Unknown command in this context')

        sock.sendto(response.encode(), addr)

start_dt_server()





