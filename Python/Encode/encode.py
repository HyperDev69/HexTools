def string2hex(input_string):
    return '-'.join(format(ord(c), 'x') for c in input_string)

input_string = input("Enter a word to encode: ")
encoded_string = string2hex(input_string)
print("Encoded in hex:", encoded_string)
