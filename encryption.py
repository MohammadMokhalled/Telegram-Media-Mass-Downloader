# encryption.py

from cryptography.fernet import Fernet
import os

ENCRYPTED_FILE = 'api_data.enc'
KEY_FILE = 'encryption_key.key'

def generate_key():
    """Generate an encryption key."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def get_cipher_suite():
    """Retrieve the cipher suite for encryption/decryption."""
    if not os.path.exists(KEY_FILE):
        key = generate_key()
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()

    return Fernet(key)

cipher_suite = get_cipher_suite()

def save_encrypted(api_id, api_hash):
    """Encrypt and save the API ID and hash."""
    data = f"{api_id}\n{api_hash}"
    encrypted_data = cipher_suite.encrypt(data.encode())

    with open(ENCRYPTED_FILE, 'wb') as file:
        file.write(encrypted_data)

def load_encrypted():
    """Load and decrypt the API ID and hash."""
    with open(ENCRYPTED_FILE, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data.split('\n')
