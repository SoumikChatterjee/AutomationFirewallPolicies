from cryptography.fernet import Fernet

def encrypt_password(key, password):
    # Generate a Fernet key from the given key
    fernet_key = Fernet(key)

    # Encrypt the password using the Fernet key
    encrypted_password = fernet_key.encrypt(password.encode())
    
    # Return the encrypted password
    return encrypted_password

def decrypt_password(key, encrypted_password):
    # Generate a Fernet key from the given key
    fernet_key = Fernet(key)

    # Decrypt the encrypted password using the Fernet key
    decrypted_password = fernet_key.decrypt(encrypted_password).decode()
    
    # Return the decrypted password
    return decrypted_password

# Example usage
# Replace 'your_key' and 'your_password' with your own values

# Generate a Fernet key
key = Fernet.generate_key()
print(key)

# Encrypt the password
password = ''
encrypted_password = encrypt_password(key, password)
print("Encrypted password:", encrypted_password)

# Decrypt the password
decrypted_password = decrypt_password(key, encrypted_password)
print("Decrypted password:", decrypted_password)