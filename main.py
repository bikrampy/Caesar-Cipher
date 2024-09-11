alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z'
            ]


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letters in original_text:
        if letters in alphabet:
            index_value = alphabet.index(letters)
            index_value += (shift_amount % 26)
            encrypted_text += alphabet[index_value]
        else:
            encrypted_text += letters
    print(encrypted_text)


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letters in original_text:
        if letters in alphabet:
            index_value = alphabet.index(letters)
            index_value -= (shift_amount % 26)
            decrypted_text += alphabet[index_value]
        else:
            decrypted_text += letters
    print(decrypted_text)


operation_continue = True

while operation_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input. Try again.")
    will_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if will_continue == "yes":
        operation_continue = True
    elif will_continue == "no":
        operation_continue = False
    else:
        print("Invalid input.")
        operation_continue = False
