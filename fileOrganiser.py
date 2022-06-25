import os
import shutil
# path = 'C:/Users/fahim/Desktop/Byjus future school python/c99'
path = input('Enter the name of the folder to be sorted:')
listOfFiles = os.listdir(path)
for i in listOfFiles:
  rootName, ext = os.path.splitext(i)
  ext = ext[1:]
  if ext == '':
    continue
  if os.path.exists(path+'/'+ext):
    shutil.move(path+'/'+i, path+'/'+ext+'/'+'/')
  else:
    os.mkdir(path+'/'+ext)
    shutil.move(path+'/'+i, path+'/'+ext+'/'+'/')