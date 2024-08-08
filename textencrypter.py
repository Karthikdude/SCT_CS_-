from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    shift = int(request.form['shift'])
    result = caesar_cipher_encrypt(text, shift)
    return render_template('index.html', result=result, operation="Encrypt")

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['text']
    shift = int(request.form['shift'])
    result = caesar_cipher_decrypt(text, shift)
    return render_template('index.html', result=result, operation="Decrypt")

if __name__ == '__main__':
    app.run(debug=True)
