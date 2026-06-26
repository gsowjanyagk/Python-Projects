from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("Password Manager\key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("Password Manager\key.key", "rb")
    key = file.read()
    file.close()
    return key

import os
if not os.path.exists("Password Manager\key.key"):
    write_key()

maspass = input("Enter your master password: ")
key = load_key() 
fer = Fernet(key)

def view():
    with open("Password Manager\passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            decrypted = fer.decrypt(pwd.encode()).decode()

            print(f"Account: {user} | Password: {decrypted}")

def add():
    accname = input("Enter the account name: ")
    pwd = input("Enter the password: ")
    
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open("Password Manager\passwords.txt", "a") as f:
        f.write(f"{accname}|{encrypted_pwd}\n")

while True:
    mode = input("Would you like to (V)iew or (A)dd a password? Q to quit. ").upper()
    if mode == "Q":
        break
    elif mode == "V":
        view()
    elif mode == "A":
        add()
    else:
        print("Invalid input. Please enter V, A, or Q.")