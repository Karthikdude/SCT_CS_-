# TextEncrypter

## Overview

`TextEncrypter` is a simple web application that allows users to encrypt and decrypt text using the Caesar cipher algorithm. Built with Flask, this application provides a user-friendly interface for performing basic text encryption and decryption operations.

## Features

- **Caesar Cipher Encryption**: Encrypts text using a shift value.
- **Caesar Cipher Decryption**: Decrypts text using a shift value.
- **Web Interface**: Built with Flask to provide a simple web interface for encryption and decryption.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Karthikdude/textencrypter.git
    cd textencrypter
    ```

2. **Install the required libraries**:
    ```bash
    pip install flask
    ```

## Usage

1. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will start and be accessible at `http://127.0.0.1:5000/`.

2. **Using the Web Interface**:
    - Navigate to the application URL in your web browser.
    - Enter the text you want to encrypt or decrypt.
    - Specify the shift value for the Caesar cipher.
    - Click on the appropriate button to encrypt or decrypt the text.

## Code Explanation

- **`app.py`**: The main file that contains the Flask application and Caesar cipher logic.
  - **Routes**:
    - `/`: Renders the main page with the input form.
    - `/encrypt`: Handles text encryption and returns the result.
    - `/decrypt`: Handles text decryption and returns the result.
  - **Caesar Cipher Functions**:
    - `caesar_cipher_encrypt(text, shift)`: Encrypts the given text using the Caesar cipher with a specified shift value.
    - `caesar_cipher_decrypt(text, shift)`: Decrypts the given text using the Caesar cipher with a specified shift value (by reversing the encryption).

- **Templates**:
  - The application uses `index.html` located in the root directory for rendering the user interface.

## Running the Application

1. **Start the Flask Application**:
    ```bash
    python app.py
    ```

2. **Access the Application**:
    Open a web browser and go to `http://127.0.0.1:5000/` to use the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## Contact

For any questions or feedback, please contact Karthik S Sathyan at karthikssathyan1@gmail.com.

