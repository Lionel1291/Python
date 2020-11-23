passwordfile = open("%SystemRoot%/system32/config/SAM", "rt")
passwords = passwordfile.open()
passwordfile.close()
print(passwords)