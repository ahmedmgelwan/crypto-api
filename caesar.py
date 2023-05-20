def caesar_cipher(message, key=3, mode='encrypt'):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  # if the letter is actually a letter
            if mode == "encrypt":
                # find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) + key) % len(alpha)
            elif mode == "decrypt":
                # find the corresponding plaintext letter in the alphabet
                letter_index = (alpha.find(letter) - key) % len(alpha)

            result += alpha[letter_index]
        else:
            result += letter

    return result

if __name__ == '__main__':
    
    key = 3
    message = "HELLO, WORLD!"

    # Encryption
    encrypted_message = caesar_cipher(key, message, "encrypt")
    print("Encrypted:", encrypted_message)

    # Decryption
    decrypted_message = caesar_cipher(key, encrypted_message, "decrypt")
    print("Decrypted:", decrypted_message)
