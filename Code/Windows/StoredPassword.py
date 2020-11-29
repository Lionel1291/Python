#import subprocess

#safedPW = subprocess.check_output(['rundll32.exe', 'keymgr.dll,KRShowKeyMgr']).decode('cp850')
#print(safedPW)
import getpass

try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)