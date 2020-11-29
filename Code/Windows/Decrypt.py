import itertools

from cryptography.fernet import Fernet
import hashlib
import string
from threading import Thread
import traceback

#for (3, 12):
    #passwd = hashlib.new('ntlm', word.strip())

with open('sam', 'rb') as decrypted_file:
    decrypted = decrypted_file.read()

all_char = string.digits + string.ascii_letters + string.punctuation
countLength = 0
countChar = 0
for i in range(1,15):
    countLength += 1
    for j in map(''.join, itertools.product(all_char, repeat=i)):
        countChar += 1
        print(str(countLength) + "           " + str(countChar))
        try:
            f = Fernet(hashlib.new('ntlm', j.strip()))
            encrypted = f.encrypt(decrypted)
            with open('sam,txt', 'wb') as encrypted_file:
                encrypted_file.write(decrypted)
        except:
            continue
        else:
            print("[+] Password found:", j.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")