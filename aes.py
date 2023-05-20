from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def aes_process(key, data, mode):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)

    if mode == 'encrypt':
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext
    elif mode == 'decrypt':
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
        return plaintext
    else:
        raise ValueError("Invalid mode. Must be 'encrypt' or 'decrypt'.")


if __name__ == '__main__':
    key = b'SupeSupeSupeSupeSupeSupeSupeSupe'  # 16, 24, or 32 bytes
    plaintext = b'Hello, world!'
    mode = 'encrypt'

    ciphertext = aes_process(key, plaintext, mode)
    decrypted_text = aes_process(key, ciphertext, 'decrypt')

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)
