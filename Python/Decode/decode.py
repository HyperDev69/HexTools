def hex2string(hex_string):
    hex_string = hex_string.replace("-", "")
    bytes_object = bytes.fromhex(hex_string)
    return bytes_object.decode("utf-8")

hex_string = input("Enter hex to decode: ")
decoded_string = hex2string(hex_string)
print("Decoded string:", decoded_string)
