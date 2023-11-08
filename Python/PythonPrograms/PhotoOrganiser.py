from PIL import Image
import shutil
import os
def get_date_taken(path):
    try:
      datetime =  str(Image.open(path)._getexif()[36867])
      completedate = datetime.split(" ")[0]
      date = completedate.split(":")
      dd = date[2]
      mm = date[1]
      months = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}
      month = months.get(mm)
      yyyy = date[0]
      try:
        os.mkdir(f"Photos of {yyyy}")
      except:
        pass
      cwd = os.getcwd()
      head, tail = os.path.split(path)
      semicomplete = f"Photos of {month} {yyyy}"
      semisemicomplete = f"{cwd}/Photos of {yyyy}/{semicomplete}"
      semicompletepath = f"{cwd}/Photos of {yyyy}/{semicomplete}/{tail}"
      try:
        os.mkdir(semisemicomplete)
        print("Copying your photos...")
        shutil.copy(path, semicompletepath)
        print("Photos copied successfully...")
        os.remove(path)
      except:
        print("Copying your photos...")
        shutil.copy(path, semicompletepath) 
        print("Photos copied successfully...")
        os.remove(path) 
    except Exception as e:
      print("There was an error...")

path = input("Enter the path of the Photos. If there are more than 1 photo, please separate by a space. Or, if you want to organise all the pictures in the current folder, type Folder")
if path == "Folder":
  from os import walk
  f = []
  for (dirpath, dirnames, filenames) in walk(os.getcwd()):
      f.extend(filenames)
      for path in f:
        get_date_taken(path)
else:
  try:
    checkpath = path.split(" ")
    for path in checkpath:
        get_date_taken(path)
  except:
    get_date_taken(path)