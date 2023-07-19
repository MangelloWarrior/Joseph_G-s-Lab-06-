def decode_string(encoded_string):
    decoded_string = ""
    for char in encoded_string:
        if char.isdigit():
 
            decoded_digit = int(char) - 3

            if decoded_digit < 0:
                decoded_digit = decoded_digit + 10

            decoded_string += str(decoded_digit)
        else:

            decoded_string += char

    return decoded_string