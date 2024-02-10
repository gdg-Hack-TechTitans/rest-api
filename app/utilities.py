import bcrypt
import secrets
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# def hash_password(password : str):
#     return bcrypt.hashpw(password.encode('utf-8'),  bcrypt.gensalt()).decode('utf-8')

    # return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

import hashlib

def hash_password(password):
    # Encode the password as bytes before hashing
    password_bytes = password.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password