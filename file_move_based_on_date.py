####################################################################################################################################################################
####################################################### This script is created by D. Niehoff #######################################################################
####################################################################################################################################################################

import os
import os.path
import shutil
import time
from datetime import datetime

#define source and destination folders
src_dir = ['C:/test', 'C:/test2']
dst_dir = ['C:/output', 'C:/output2']

##############################################################################################################################################################

#the actual function what will check and move files if possible

def file_move(src, dst):

#Delete old content of logfile and add timestamp
    logfile= open(os.path.join(src, "logfile.txt"),"w")
    logfile.write('Script performed on: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    logfile.close() 

#change current work directory
    os.chdir(src)

#list through all files in directory
    if os.listdir(src):
        for file in os.listdir('.'):
            if not file == 'logfile.txt':
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

#check if file already excist on destination
                check_file = os.path.join(folder, file)
                if not os.path.isfile(check_file):

#move file to destination
                    dst_year_mont = os.path.join(dst, year, month)                                  #determine destination folder based on year and month
                    shutil.move(file, dst_year_mont);
                else:
#Add file name to logfile
                    logfile= open(os.path.join(src, "logfile.txt"),"a")
                    logfile.write(file + ' Already exist on destination' + '\n')
                    logfile.close() 

###############################################################################################################################################################

#Looping through move function with provided folders
for (src,dst) in zip(src_dir, dst_dir):
        file_move(src, dst)
