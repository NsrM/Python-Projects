import os
import datetime
from os import walk

class FindOldFiles:

    def filesOlderthanYear(self):
        str=datetime.datetime.now()
        filelist=[]
        filepath="/home/naseer/Python"
        for (dirpath,dirname,filenames) in walk("/home/naseer/Python"):
            filelist.extend(filenames)
            print("The standard datetime format is ",end=" ")
            print(str)
            break
        print("The files which are one year or more old")

        for i in range(len(filenames)):

                str1=os.path.getmtime(filepath+"/"+filenames[i])
                str1=datetime.datetime.fromtimestamp(str1)
                # print((str-str1).days)
                if((str-str1).days>=365):
                    print(filenames[i]+"  ",end=" ")
                    print(str1)




p=FindOldFiles()
p.filesOlderthanYear()
