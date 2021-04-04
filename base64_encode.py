# Conversion array
base64_array = []
for i in range(65, 90+1):
    base64_array.append(chr(i))
for i in range(97, 122+1):
    base64_array.append(chr(i))
for i in range(0, 9+1):
    base64_array.append(str(i))
base64_array.append('+')
base64_array.append('/')

msg_to_encode = input('Encode this : ')

# Build binary representation of string
binary_string = ""
for char in msg_to_encode:
    binary_string += bin(ord(char))[2:].rjust(8, '0')

# Regular encoding of 6-bits chunks
encoded = ""
for i in range(0, len(binary_string), 6):  # Index goes up by 6 every time
    encoded += base64_array[int(binary_string[i:i+6], 2)]

# Handle remaining bits
remaining_count = len(binary_string) % 6
if remaining_count != 0:
    encoded = encoded[:-1]  # Last encoded char is wrong, remove it
    # Zero-fill last bits
    binary_remaining = binary_string[-1*remaining_count:].ljust(6, '0')
    encoded += base64_array[int(binary_remaining, 2)]  # Encode last bits
    # Add the '=' needed to indicate the zero-filled bits
    encoded += '='*int((6-remaining_count)/2)

print(encoded)
