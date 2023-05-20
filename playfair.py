import re

def playfair_cipher(key, plaintext, mode='encrypt'):
    key = key.upper()
    plaintext = re.sub(r'[^A-Z]', '', plaintext.upper())
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_matrix = generate_key_matrix(key)

    if mode == 'encrypt':
        ciphertext = encrypt(plaintext, key_matrix, alphabet)
    elif mode == 'decrypt':
        ciphertext = decrypt(plaintext, key_matrix, alphabet)
    else:
        raise ValueError("Invalid mode. Choose either 'encrypt' or 'decrypt'.")

    return ciphertext

def generate_key_matrix(key):
    key = re.sub(r'[^A-Z]', '', key.upper())
    key = key.replace('J', 'I')
    key += ''.join(ch for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if ch not in key)

    key_matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def encrypt(plaintext, key_matrix, alphabet):
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        row1, col1 = get_position(pair[0], key_matrix)
        row2, col2 = get_position(pair[1], key_matrix)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ciphertext += key_matrix[row1][col1] + key_matrix[row2][col2]

    return ciphertext

def decrypt(ciphertext, key_matrix, alphabet):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        row1, col1 = get_position(pair[0], key_matrix)
        row2, col2 = get_position(pair[1], key_matrix)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        plaintext += key_matrix[row1][col1] + key_matrix[row2][col2]

    return plaintext

def get_position(char, key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j

    raise ValueError(f"Character '{char}' not found in the key matrix.")
