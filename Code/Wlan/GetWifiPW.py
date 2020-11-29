import subprocess

PWinFile = open("WifiPasswords.txt", "w")

# Deutsche Sprache
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850').split('\n')
wifis = [line.split(":")[1][1:-1] for line in data if  "Profil für alle Benutzer" in line]
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp850').split('\n')
    results = [line.split(":")[1][1:-1] for line in results if 'Schlüsselinhalt' in line]
    try:
        PWinFile.write(f'Name: {wifi}, Password: {results[0]}')
        PWinFile.write("\n")
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannot be read!')
        PWinFile.write(f'Name: {wifi}, Password: Cannot be read!')
        PWinFile.write("\n")


# Englische Sprache
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp850').split('\n')
wifis = [line.split(":")[1][1:-1] for line in data if  "All User Profile" in line]
PWinFile = open("WifiPasswords.txt", "w")
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp850').split('\n')
    results = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]
    try:
        PWinFile.write(f'Name: {wifi}, Password: {results[0]}')
        PWinFile.write("\n")
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannot be read!')
        PWinFile.write(f'Name: {wifi}, Password: Cannot be read!')
        PWinFile.write("\n")

PWinFile.close()