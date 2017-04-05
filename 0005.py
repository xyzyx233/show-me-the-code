# coding:utf-8 -*-
import os
from PIL import Image

class resizeimg:
    def __init__(self):
        self.filelist=[]
        self.oldpath='rabiribi/'
        self.newpath='newsize/'

    def getfilelist(self):
        self.filelist=os.listdir(self.oldpath)

    def resizepic(self):
        for im in self.filelist:
            re=Image.open(self.oldpath+im)
            (x,y)=re.size
            x_s=190
            y_s=y*x_s/x
            out=re.resize((x_s,y_s),Image.ANTIALIAS)
            # out.show()
            out.save(self.newpath+'new_'+im)

r=resizeimg()
r.getfilelist()
r.resizepic()