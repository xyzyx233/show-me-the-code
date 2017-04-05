# -*- coding:utf-8 -*-

import redis

class redisdb:
    def __init__(self):
        self.r=redis.Redis()
        self.codelist=[]
        self.filename="activitecode.txt"

    def readcode(self):
        f=open(self.filename)
        while 1:
            l=f.readline()
            self.codelist.append(l)
            if not l:
                break

    def setdata(self):
        x=1
        for i in self.codelist:
            self.r.set(str(x),i)
            x=x+1

    def getdata(self):
        for x in range(1,201):
            print self.r.get(str(x))

xx=redisdb()
xx.readcode()
xx.setdata()
xx.getdata()