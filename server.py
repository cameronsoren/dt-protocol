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

# Use the same bytes for context-switching as data bytes
def check_for_context_switch(byte_value, current_context):
    # Define potential context-switching conditions
    # We're reusing the same byte values (e.g., 0x01) for context switching
    if byte_value == 0x01 and current_context == 'user':
        return 'product'
    elif byte_value == 0x01 and current_context == 'product':
        return 'device_info'
    elif byte_value == 0x01 and current_context == 'device_info':
        return 'control'
    elif byte_value == 0x01 and current_context == 'control':
        return 'user'
    else:
        return None  # No context switch

def start_dt_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 9999))

    print("dt Protocol Server is running...")

    # Initialize context to 'user'
    current_context = 'user'

    while True:
        data, addr = sock.recvfrom(1)  # Receive 1 byte
        byte_value = data[0]

        # Check if the byte should switch context
        new_context = check_for_context_switch(byte_value, current_context)

        if new_context:  # If the byte is for context-switching
            current_context = new_context
            response = f"Switched to {current_context} context"
        else:
            # Fetch the appropriate response based on the current context
            response = context_maps[current_context].get(byte_value, 'Unknown command in this context')

        sock.sendto(response.encode(), addr)

start_dt_server()



