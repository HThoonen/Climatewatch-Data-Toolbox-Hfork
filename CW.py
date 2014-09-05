from PIL import Image, ImageTk
from csv import *
import Tkinter as Tk
import urllib2
import ttk
import io
import os

def magbanish(filein,fileout):
    fileGet = open(filein,"r")
    fileSet = open(fileout,"w")
    data=reader(fileGet)
    stringCreate=""
    imgtry = 0
    imgget = 0
    imgfail = 0
    
    for item in data:
        if (item[16] == "No") & (item[15] == "Bird on Nest"):
            for d in item:
                stringCreate=stringCreate + d + ","
            stringCreate=stringCreate + "\n"
        if item[13] != "associatedMedia":
            if item[13] != "":
                imgtry = imgtry + 1
                try:
                    magimg = urllib2.urlopen(item[13])
                    image_file = io.BytesIO(magimg.read())
                    pil_image = Image.open(image_file)
                    tkwindow = Tk.Tk()
                    imgw, imgh = pil_image.size
                    image_tk = ImageTk.PhotoImage(pil_image.resize(((imgw/10), (imgh/10))))
                    jwin = ttk.Label(image=image_tk)
                    jwin.pack()
                    #tkwindow.mainloop()
                    imgget = imgget + 1
                    print "tried " + str(object=imgtry)
                except urllib2.HTTPError:
                    imgfail = imgfail + 1
                    print "Image not found"
                    print "tried " + str(object=imgtry)
    print stringCreate
    print "Images sought: " + str(object=imgtry)
    print "Images found: " + str(object=imgget)
    print "Images lost: " + str(object=imgfail)
    
    fileSet.write(stringCreate)
    fileSet.close()

stringin = raw_input("Location of input file: ")
stringout = raw_input("Location of output file: ")
magbanish(stringin,stringout)
