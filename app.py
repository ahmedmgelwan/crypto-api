from flask import Flask, render_template, request
from playfair import playfair_cipher
from vig import vigenere_cipher
from aes import aes_process
from rsa import rsa_process
from sha import sha256_hash, sha512_hash
from caesar import caesar_cipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        shifts = int(request.form['shifts'])
        operation = request.form['operation']

        ciphertext = caesar_cipher(plaintext, shifts, operation)
        

        return render_template('caesar.html', ciphertext=ciphertext)

    return render_template('caesar.html')

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        operation = request.form['operation']

        ciphertext = vigenere_cipher(key, plaintext, mode=operation)

        return render_template('vigenere.html', ciphertext=ciphertext)
    return render_template('vigenere.html')

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    if request.method == 'POST':
        plaintext = request.form['plaintext'].replace(' ', '')
        key = request.form['key']
        operation = request.form['operation']
        
        ciphertext = playfair_cipher(key, plaintext, operation)

        return render_template('playfair.html', ciphertext=ciphertext)
    
    return render_template('playfair.html')

@app.route('/aes', methods=['GET', 'POST'])
def aes():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        operation = request.form['operation']

        ciphertext = vigenere_cipher(key, plaintext, mode=operation)

        return render_template('aes.html', ciphertext=ciphertext)
    return render_template('aes.html')

@app.route('/rsa', methods=['GET', 'POST'])
def rsa():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        operation = request.form['operation']

        ciphertext = vigenere_cipher(key, plaintext, mode=operation)

        return render_template('rsa.html', ciphertext=ciphertext)
    return render_template('rsa.html')

@app.route('/blowfish', methods=['GET', 'POST'])


@app.route('/sha', methods=['GET', 'POST'])
def sha():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        size = request.form['sha-type']
        hashed = sha256_hash(plaintext) if size == 'sha256' else sha512_hash(plaintext)
        return render_template('sha.html', hashed=hashed)
    return render_template('sha.html')



if __name__ == '__main__':
    app.run(debug=False)
