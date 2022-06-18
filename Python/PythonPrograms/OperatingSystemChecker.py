from sys import platform
if platform == "linux" or platform == "linux2":
    print ('You are using a Linux System')
elif platform == "darwin":
    print ('You are using a MacOS System')
elif platform == "win32":
    print ('You are using a Windows System')