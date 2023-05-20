import string

def vigenere_cipher(key, plaintext, mode='encrypt'):
    key = key.upper()
    plaintext = plaintext.upper()
    alphabet = string.ascii_uppercase
    key_length = len(key)
    ciphertext = ""

    for i, char in enumerate(plaintext):
        if char in alphabet:
            key_char = key[i % key_length]
            if mode == 'encrypt':
                shift = (alphabet.index(char) + alphabet.index(key_char)) % 26
            else:
                shift = (alphabet.index(char) - alphabet.index(key_char)) % 26
            ciphertext += alphabet[shift]
        else:
            ciphertext += char

    return ciphertext

# Example usage

if __name__ == '__main__':
    key = 'SECRET'
    plaintext = 'HELLO WORLD'
    encrypted_text = vigenere_cipher(key, plaintext, mode='encrypt')
    decrypted_text = vigenere_cipher(key, encrypted_text, mode='decrypt')

    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
