#This program uses the System Timings and automatically activates Dark Mode
import datetime as dt
import sys, shutil, os, time

AppDAta = os.getenv('APPDATA')

print("Welcome to Auto Dark Mode!\n")
if os.path.isfile(os.path.join(AppDAta, "Microsoft/Windows/Start Menu/Programs/Startup", "AutoDarkMode.py")):  # type: ignore
    pass
else:
    print("Add this App to startup?")
    while True:
        q = input("Enter Y or N")
        if q == "Y":
            path = sys.argv[0]
            shutil.copy(path, os.path.join(AppDAta, "Microsoft/Windows/Start Menu/Programs/Startup", "AutoDarkMode.py"))  # type: ignore
            print("Added successfully")
            break
        if q == "N":
            print("Ok")
            break

while True:
    current_hour = int(((str(dt.datetime.now()).split(" ")[1]).split(".")[0]).split(":")[0])
    if current_hour >= 18:
        print("Activate Dark Mode")
        os.system(r"reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f")
    else:
        print("Activate Light Mode")
        os.system(r"reg.exe add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f")
    time.sleep(60)
    continue
