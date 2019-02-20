####################################################################################################################################################################
# This script is created by D. Niehoff
# The purpose of the script is to automatically move files in the year - month folder structure based on the creation date of the file
# The intention is to have this script run on a Synology server
# Below you can find the open actions for this script
####################################################################################################################################################################

import os
import os.path
import shutil
import time

#define
src = 'C:/test'																				#source folder
dst = 'C:/output'																			#destination folder
os.chdir(src)																				#change current work directory

#list through all files in directory
if os.listdir(src):
    for file in os.listdir('.'):
        filedate = time.gmtime(os.path.getmtime(file))                                      #get metadata from file
        year = str(filedate.tm_year)                                                        #make string from year
        month = str(filedate.tm_mon)                                                        #make string from month

#check if year folder already exist if not create one
        folder = os.path.join (dst, year)                                                   #define folder based on year
        if not os.path.isdir(folder):
            os.mkdir(folder)

#check if month folder already exist within year folder if not create one
        folder = os.path.join (folder, month)                                               #define folder based on month within year
        if not os.path.isdir(folder):
            os.mkdir(folder)

#move file to destination
        dst_year_mont = os.path.join(dst, year, month)                                  #determine destination folder based on year and month
        shutil.move(file, dst_year_mont);

################################################################ Version ##########################################################################################
# V1.0 First working version just copying from source to destination folder
#
################################################################# to do ###########################################################################################
# 1. check if file already exist in folder before copy or overwrite file
# 2. Have this script go through different source folders
# 3. On error go to next
# 4. Create logfile in source directory when script is performed
# 5. Better error handling
###################################################################################################################################################################
