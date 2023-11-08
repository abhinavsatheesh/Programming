import os
import sys
import shutil
import threading
import time
import errno
import stat

def StandardMode():
    print("Welcome to Identical File Checker. \nThis script is designed to check if two folders have the same no. of files and sub-folders. This is primarily\n useful, when you need to backup your folder to different places like OneDrive, your USB and more. The program will prompt you to enter the locations of 2 folders - Folder A and Folder B")
    path_a = input("Enter the path of Folder A : ")
    while True:
        if os.path.isdir(path_a):
            break
        else:
            path_a = input("That's an invalid path. Enter the path of Folder A : ")
    path_b = input("Enter the path of Folder B : ") 
    while True:
        if os.path.isdir(path_b):
            break
        else:
            path_b = input("That's an invalid path. Enter the path of Folder B : ")
    print(f"\nFolder A - {path_a}")
    print(f"Folder B - {path_b}\n")
    print(f"Calculating the no. of files and folders in Folder A - {path_a}")
    HOME_FOLDER = path_a
    noOfFilesA = 0
    noOfDirA = 0

    for base, dirs, files in os.walk(HOME_FOLDER):
        for directories in dirs:
            noOfDirA += 1
        for Files in files:
            noOfFilesA += 1

    print('Number of files',noOfFilesA)
    print('Number of Directories',noOfDirA)
    print("---------------")
    print(f"Calculating the no. of files and folders in Folder B - {path_b}")
    HOME_FOLDER = path_b
    noOfFilesB = 0
    noOfDirB = 0

    for base, dirs, files in os.walk(HOME_FOLDER):
        for directories in dirs:
            noOfDirB += 1
        for Files in files:
            noOfFilesB += 1

    print('Number of files',noOfFilesB)
    print('Number of Directories',noOfDirB,"\n")

    if noOfFilesB == noOfFilesA:
        print("No. of files in Folder A and Folder B are the same")
    else:
        print("No. of files in Folder A and Folder B are not the same")

    if noOfDirB == noOfDirA:
        print("No. of sub-directories in Folder A and Folder B are the same")
    else:
        print("No. of sub-directories in Folder A and Folder B are not the same")

    question = input("\nDo you wish to enter Advanced Mode?\nWith Advanced Mode, you can export the File Details to a Text File, Advanced Comparisons and more.\nEnter Y to enter Advanced Mode")
    if question == "Y":
        print("Entering Advanced Mode....")
        AdvancedMode(path_a, path_b)
    else:
        print("Exiting Identical File Checker. Thank You for using it")
        exit()

def AdvancedMode(folderA, folderB):
    print("\nWelcome to Advanced Mode")       
    question = input(f"Continue with Folder A as {folderA} and Folder B as {folderB}?\nEnter Y to confirm, or else enter N to select another Folder")
    if question == "Y":
        print("Ok")
        with open(os.path.join(".", "IdenticalFileCheckerLog.txt"), "w+") as file1:
            file1.write(f"Folder A - {folderA}\n")
            HOME_FOLDER = folderA
            noOfFilesA = 0
            noOfDirA = 0

            for base, dirs, files in os.walk(HOME_FOLDER):
                for directories in dirs:
                    noOfDirA += 1
                for Files in files:
                    noOfFilesA += 1
            file1.write(f"Files : {noOfFilesA}\nFolders : {noOfDirA}\n")
            file1.write(f"Folder B - {folderB}\n")
            HOME_FOLDER = folderB
            noOfFilesB = 0
            noOfDirB = 0
            for base, dirs, files in os.walk(HOME_FOLDER):
                for directories in dirs:
                    noOfDirB += 1
                for Files in files:
                    noOfFilesB += 1
            file1.write(f"Files : {noOfFilesB}\nFolders : {noOfDirB}\n")          
        Files_Folders_inA = os.listdir(folderA)
        Files_Folders_inB = os.listdir(folderB)
        NotFound_Files = {}
        for Files_In_A in Files_Folders_inA:
            tempPath = os.path.join(folderB, Files_In_A)
            with open(os.path.join(".", "IdenticalFileCheckerLog.txt"), "a") as file1:
                pass
                if os.path.isfile(tempPath):
                    print(f"[FILE] : {Files_In_A} found in Folder A and Folder B")
                    file1.write(f"\n[FILE] : {Files_In_A} found in Folder A and Folder B")
                elif os.path.isdir(tempPath):
                    print(f"[FOLDER] : {Files_In_A} found in Folder A and Folder B")
                    file1.write(f"\n[FOLDER] : {Files_In_A} found in Folder A and Folder B")
                elif os.path.exists(tempPath) == False:
                    print(f"[NOT FOUND] : {Files_In_A} does not exist in Folder B")
                    file1.write(f"\n[NOT FOUND] : {Files_In_A} does not exist in Folder B") 
        file1.close()      
        print("\nDetails of the operation has been logged in a file called IdenticalFileCheckerLog.txt in the Current Working Directory\n")          
        question = input("Do you wish to copy the files from Folder A which are not present in Folder B? \nThis will eventually make both folders have the same no. of sub-files and sub-folders. Press Y to copy, and N to cancel")      
        if question == "Y":
            warning = input("WARNING! This will delete all the contents of Folder B, and all the files from Folder A will be copied to Folder B. Are you sure you wish to continue? Press Y to enter, press N to exit")
            if warning == "Y":
                def handleRemoveReadonly(func, path, exc):
                    excvalue = exc[1]
                    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
                        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                        func(path)
                    else:
                        raise

                des = folderB
                src = folderA
                try:
                    shutil.rmtree(des, ignore_errors=False, onerror=handleRemoveReadonly)
                except:
                    pass

                def checker(source_path, destination_path):
                    while not os.path.exists(destination_path):
                        time.sleep(.01)

                    while os.path.getsize(source_path) != os.path.getsize(destination_path):
                        print (int((float(os.path.getsize(destination_path))/float(os.path.getsize(source_path))) * 100), "%")
                        time.sleep(.01)

                    print ("100 %")


                def copying_file(source_path, destination_path):
                    print ("Copying all files from Folder A to Folder B.....")
                    shutil.copytree(source_path, destination_path)

                    if os.path.exists(destination_path):
                        print ("Copied all the files from Folder A to Folder B. The no. of files and sub-directories in Folder B is the same as Folder A")
                        print("Exiting Identical File Checker. Thank You for using it")
                        return True
                        exit()
                        

                    print ("Failed...")
                    return False


                t = threading.Thread(name='Copying', target=copying_file, args=(src, des))
                # Start the copying on a separate thread
                t.start()
                # Checking the status of destination file on a separate thread
                b = threading.Thread(name='checking', target=checker, args=(src, des))
                b.start()
            else:
                print("Exiting Identical File Checker. Thank You for using it")
                exit()
        else:
            print("Exiting Identical File Checker. Thank You for using it")
            exit()
    elif question == "N":
        path_a = input("Enter the path of Folder A : ")
        while True:
            if os.path.isdir(path_a):
                break
            else:
                path_a = input("That's an invalid path. Enter the path of Folder A : ")
        path_b = input("Enter the path of Folder B : ") 
        while True:
            if os.path.isdir(path_b):
                break
            else:
                path_b = input("That's an invalid path. Enter the path of Folder B : ")
        print(f"\nFolder A - {path_a}")
        print(f"Folder B - {path_b}\n")
        folderA = path_a
        folderB = path_b
        with open(os.path.join(".", "IdenticalFileCheckerLog.txt"), "w+") as file1:
            file1.write(f"Folder A - {folderA}\n")
            HOME_FOLDER = folderA
            noOfFilesA = 0
            noOfDirA = 0

            for base, dirs, files in os.walk(HOME_FOLDER):
                for directories in dirs:
                    noOfDirA += 1
                for Files in files:
                    noOfFilesA += 1
            file1.write(f"Files : {noOfFilesA}\nFolders : {noOfDirA}\n")
            file1.write(f"Folder B - {folderB}\n")
            HOME_FOLDER = folderB
            noOfFilesB = 0
            noOfDirB = 0
            for base, dirs, files in os.walk(HOME_FOLDER):
                for directories in dirs:
                    noOfDirB += 1
                for Files in files:
                    noOfFilesB += 1
            file1.write(f"Files : {noOfFilesB}\nFolders : {noOfDirB}\n")
            file1.close()
            if noOfFilesA == noOfFilesB and noOfDirA == noOfDirB:
                pass
            else:
                pleaseShow = True
        Files_Folders_inA = os.listdir(folderA)
        Files_Folders_inB = os.listdir(folderB)
        for Files_In_A in Files_Folders_inA:
            tempPath = os.path.join(folderB, Files_In_A)
            with open(os.path.join(".", "IdenticalFileCheckerLog.txt"), "a") as file1:
                pass
                if os.path.isfile(tempPath):
                    print(f"[FILE] : {Files_In_A} found in Folder A and Folder B")
                    file1.write(f"\n[FILE] : {Files_In_A} found in Folder A and Folder B")
                elif os.path.isdir(tempPath):
                    print(f"[FOLDER] : {Files_In_A} found in Folder A and Folder B")
                    file1.write(f"\n[FOLDER] : {Files_In_A} found in Folder A and Folder B")
                elif os.path.exists(tempPath) == False:
                    print(f"[NOT FOUND] : {Files_In_A} does not exist in either Folder A or Folder B")
                    file1.write(f"\n[NOT FOUND] : {Files_In_A} found in Folder A and Folder B") 
        file1.close()     
        print("\nDetails of the operation has been logged in a file called IdenticalFileCheckerLog.txt in the Current Working Directory\n")          
       
        question = input("Do you wish to copy the files from Folder A which are not present in Folder B? \nThis will eventually make both folders have the same no. of sub-files and sub-folders. Press Y to copy, and N to cancel")      
        if question == "Y":
            warning = input("WARNING! This will delete all the contents of Folder B, and all the files from Folder A will be copied to Folder B. Are you sure you wish to continue? Press Y to enter, press N to exit")
            if warning == "Y":
                def handleRemoveReadonly(func, path, exc):
                    excvalue = exc[1]
                    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
                        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                        func(path)
                    else:
                        raise

                des = folderB
                src = folderA
                try:
                    shutil.rmtree(des, ignore_errors=False, onerror=handleRemoveReadonly)
                except:
                    pass

                def checker(source_path, destination_path):
                    # Making sure the destination path exists
                    while not os.path.exists(destination_path):
                        time.sleep(.01)

                    # Keep checking the file size till it's the same as source file
                    while os.path.getsize(source_path) != os.path.getsize(destination_path):
                        print (int((float(os.path.getsize(destination_path))/float(os.path.getsize(source_path))) * 100), "%")
                        time.sleep(.01)

                    print ("100 %")


                def copying_file(source_path, destination_path):
                    print ("Copying all files from Folder A to Folder B.....")
                    shutil.copytree(source_path, destination_path)

                    if os.path.exists(destination_path):
                        print ("Copied all the files from Folder A to Folder B. The no. of files and sub-directories in Folder B is the same as Folder A")
                        print("Exiting Identical File Checker. Thank You for using it")
                        return True
                        exit()
                        

                    print ("Failed...")
                    return False


                t = threading.Thread(name='Copying', target=copying_file, args=(src, des))
                # Start the copying on a separate thread
                t.start()
                # Checking the status of destination file on a separate thread
                b = threading.Thread(name='checking', target=checker, args=(src, des))
                b.start()
            else:
                print("Exiting Identical File Checker. Thank You for using it")
                exit()
        else:
            print("Exiting Identical File Checker. Thank You for using it")
            exit()
    else:
        print("Exiting Identical File Checker. Thank You for using it")
        exit()
        
if __name__ == "__main__":
    StandardMode()