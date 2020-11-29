import subprocess
#cipher /d /s:"full path of folder"
subprocess.check_output(['cipher', '/d', '"C:\sam"']).decode('cp850')