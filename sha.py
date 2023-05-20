import hashlib

def sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def sha512_hash(data):
    hash_object = hashlib.sha512(data.encode())
    return hash_object.hexdigest()

if __name__ == '__main__':

    data = "Hello, World!"

    sha256_result = sha256_hash(data)
    sha512_result = sha512_hash(data)

    print("SHA-256 Hash:", sha256_result)
    print("SHA-512 Hash:", sha512_result)
