# tyler squires

def encode(code):
    encoded = ""
    for char in code:
        new = int(char) + 3
        if new > 9:
            encoded += str(new)[1]
        else:
            encoded += str(new)
    return encoded

if __name__ == '__main__':
    encoded = ""
    decoded = ""
    while True:
        option = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if int(option) == 3:
            break
        if int(option) == 2:
            print(f"The encoded password is {encoded}, and the original password is {decoded}\n")
        if int(option) == 1:
            code = input("Please enter your password to encode: ")
            decoded = code
            encoded = encode(code)
            print("Your password has been encoded and stored!\n")