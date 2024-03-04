# a - z = 97 - 122
# A - Z = 65 - 90

# encrption function
def encryption(message, shift_number):
    messageInArr = [char for char in message]
    encodedMessage = []
    for letter in messageInArr:
        ascii = ord(letter) + int(shift_number)
        if (letter.isupper()):
            if (ascii > 90):
                ascii = (int(ascii) - 90) + 65
        else:
            if (ascii > 122):
                ascii = (int(ascii) - 122) + 97

        encodedMessage.append(chr(ascii))

    return "".join(encodedMessage)

# decryption function


def decryption(message, shift_number):
    messageInArr = [char for char in message]
    decodedMessage = []
    for letter in messageInArr:
        ascii = ord(letter) - int(shift_number)
        if (letter.isupper()):
            if (ascii < 65):
                ascii = 90 - (65 - int(ascii))
        else:
            if (ascii < 97):
                ascii = 122 - (97 - int(ascii))
        decodedMessage.append(chr(ascii))

    return "".join(decodedMessage)


switch = True
while (switch):
    menu = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (menu == 'encode' or menu == 'decode'):
        message = input("Type your message:\n")
        shift_number = input("Type the shift number:\n")

        if (menu == 'encode'):
            result = encryption(message, shift_number)
        elif (menu == 'decode'):
            result = decryption(message, shift_number)
    else:
        print('INVALID INPUT!!')
        continue

    print(f"Here is the {menu}d message: {result}")
    descision = True
    while (descision):
        further_descision = input('Do you want to continue...?(y/n)')
        if (further_descision.lower() == 'y'):
            descision = False
        elif (further_descision.lower() == 'n'):
            descision = False
            switch = False
        else:
            print("INVALID INPUT!!")
