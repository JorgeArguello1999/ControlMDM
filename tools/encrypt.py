import bcrypt

# Encrypt your password 
def encrypt_password(password:str) -> str: 
    hash_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    return hash_password

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

if __name__ == '__main__':
    data = verify_password(
        "Jorge",
        "$2b$12$/g.4R/HFvZsT8ulVrUtMluYkPgrtuIQ4hc/IwHKqoxSeS7fWAWNB2"
    )
    print(data)