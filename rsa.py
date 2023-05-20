from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def rsa_process(key, data, mode):
    if mode == "encrypt":
        ciphertext = key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext.hex()
    elif mode == "decrypt":
        plaintext = key.decrypt(
            bytes.fromhex(data),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode('utf-8')
    else:
        raise ValueError("Invalid mode. Supported modes: 'encrypt', 'decrypt'")

# Example usage
plaintext = "Hello, World!"

try:
    private_key, public_key = generate_rsa_key_pair()

    encrypted_text = rsa_process(public_key, plaintext, mode="encrypt")
    decrypted_text = rsa_process(private_key, encrypted_text, mode="decrypt")

    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

except Exception as e:
    print("Error:", str(e))
