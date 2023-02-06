from caesar.caesarart import logo

print(logo)


def encrypt(text, shift):
    characters = list(text)
    for i in range(len(text)):
        characters[i] = chr(ord(characters[i]) + shift)
    encrypted_word = "".join(characters)
    print("The encrypted word is", encrypted_word)


def decrypt(text, shift):
    characters = list(text)
    for i in range(len(text)):
        characters[i] = chr(ord(characters[i]) - shift)
    decrypted_word = "".join(characters)
    print("The encrypted word is", decrypted_word)


use_again = True
while use_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    use = input("Do you want to use the caesar cipher again? (Yes/No) ").lower()
    if use == "no":
        use_again = False
