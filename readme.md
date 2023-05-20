# Crypto API 

Crypto API is a Python project that provides a collection of encryption and hashing algorithms. It offers functionalities to encrypt and decrypt messages using various ciphers and perform secure hash calculations. This documentation will guide you through the algorithms, libraries used, and instructions on how to set up and use the app.

## Algorithms

The Crypto API includes the following algorithms:

1. Caesar Cipher: A simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions down the alphabet.
2. Playfair Cipher: A manual symmetric encryption technique that uses a 5x5 square grid of letters and a set of rules to encrypt and decrypt messages.
3. Vigenère Cipher: A polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt text, combining elements of both substitution and polyalphabetic ciphers.
4. AES (Advanced Encryption Standard): A symmetric encryption algorithm widely used for secure communication and data protection.
5. RSA: A widely used public-key encryption algorithm based on the difficulty of factoring large integers.
6. SHA (Secure Hash Algorithm): A family of cryptographic hash functions that generate a fixed-size hash value from input data.

## Libraries

The Crypto API utilizes the following libraries:

- `Flask`: A micro web framework used for building the API endpoints and handling HTTP requests.

- `cryptography`: A popular Python library for various cryptographic operations, including AES, Blowfish, SHA, and RSA implementations.

## Setup

To set up the Crypto API, follow the steps below:

1. Clone the GitHub repository:

```shell
git clone https://github.com/ahmedmgelwan/crypto-api.git
```

Install the required dependencies using `pip`:

```shell
pip install -r requirements.txt
```

Start the server:

```shell
python app.py
```

The API will be accessible at `http://localhost:5000`.

## Contributions

Contributions to the Crypto API project are welcome! If you have suggestions, bug fixes, or additional features to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Make the desired changes in your local repository.
3. Commit and push your changes to your forked repository.
4. Submit a pull request with a clear description of your changes.

## License

The Crypto API is released under the [MIT License](https://opensource.org/licenses/MIT).

------

Designed with ❤️ by Ahmed Gelwan.