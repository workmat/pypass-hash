import bcrypt
import getpass

def hash_password():
    """
    Interactively hash a password for storing in a Docker Compose file.
    
    Returns:
        str: Bcrypt hashed password
    """
    # Prompt securely for password
    password = getpass.getpass("Enter password to hash: ")
    
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Decode to string for easy use in config files
    return hashed_password.decode('utf-8')

# Run the hashing process
if __name__ == "__main__":
    hashed_pass = hash_password()
    print(f"Hashed password: {hashed_pass}")