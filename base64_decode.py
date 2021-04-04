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

msg_to_decode = input('Decode this : ')

binary_string = ""
for char in msg_to_decode:
    if char == '=':  # '=' indicates two binary 0s
        binary_string += '00'
    else:  # Unpack regular chars as 6 bits
        binary_string += bin(base64_array.index(char))[2:].rjust(6, '0')

# Decode bytes as chars
decoded = ""
for i in range(0, len(binary_string), 8):
    decoded += chr(int(binary_string[i:i+8], 2))

print(decoded)
