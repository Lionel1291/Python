import subprocess
import win32com.shell.shell as shell
from pathlib import Path
users = [x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()]

for user in users:
    try:
        #data = subprocess.call(['net', 'user', user, 'muster']).decode('cp850')
        commands = 'net user ' + user + ' admin'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
    except IndexError:
        print(IndexError)
print(users)