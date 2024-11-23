import bcrypt

# Encrypt your password 
def encrypt_password(password:str) -> str: 
    hash_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    return hash_password

