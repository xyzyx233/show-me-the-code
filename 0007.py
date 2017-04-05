# -*- coding:utf-8 -*-
import os

class countline:
    def __init__(self):
        self.filelist=[]
        self.path='G:\\Pythonproject\\pixiv2.0-master\\'

    def getfilelist(self):
        s=os.listdir(self.path)
        a= self.endWith('.py')
        f_file=filter(a,s)
        for x in f_file:
            self.filelist.append(x)
        print self.filelist

    def endWith(selfs,*endstring):  #*任意个无名字参数——>list？ **任意个有名字参数——>字典？
        ends=endstring
        def run(s):
            f=map(s.endswith,ends)
            if True in f:
                return s
        return run

    def countline(self):
        count = 0
        for x in self.filelist:
            filep=self.path+x
            count += len(open(filep,'rU').readlines())
        print 'lines:',count

xxx=countline()
xxx.getfilelist()
xxx.countline()