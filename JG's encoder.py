
encoding_process = True
def encode_string(string):   # @ Jackson - add comments as commits

    encoded_string = ""

    for x in string:

        if x.isdigit():
            x = int(x) + 1
            encoded_string += str(x)

        else:
            encoded_string += x

    return print(f"Your string has been encoded as: {encoded_string}")


'''def decode_string(encoded_string):     #
    decoded_string = ''
    for character in encoded_string:
        if character:
'''


if __name__ == '__main__':

    while encoding_process == True:
        print("MENU: \nOption 1: Encode a String: \n\nOption 2: Decode a String: \n\nOption 3: Exit Program: ")
        option_selected = int(input("\nEnter menu option here: "))

        if option_selected == 1:
            initial_string = ((input("Input String here: ")))
            (encode_string(initial_string))

        elif option_selected == 2:
            initial_string = input('Enter string to decode: ')

        elif option_selected == 3:
            print("Exiting Program, Goodbye")
            break
        else:
            print("Invalid Selection, please enter a digit beteween 1-3")
            continue


