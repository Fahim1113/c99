import os
import shutil
#source = 'C:/Users/fahim/Desktop/Byjus future school python/c99/testFolder'
#destination = 'C:/Users/fahim/Desktop/Byjus future school python/c99/video'
source = input('Enter Source Folder Name:')
destination = input('Enter Destination Folder Name:')
source +='/'
destination +='/'
listOfFiles = os.listdir(source)
for i in listOfFiles:
  shutil.copy(source+i,destination)