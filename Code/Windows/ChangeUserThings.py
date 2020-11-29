import subprocess
from pathlib import Path
users = [x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()]

for user in users:
    if(user == 'testuser'):
        try:
            data = subprocess.call(['net', 'user', user, '*']).decode('cp850')
            print('password')
            print('password')
        except IndexError:
            print(IndexError)
print(users)