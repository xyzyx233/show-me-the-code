# -*- coding:utf-8 -*-
import string

class countletter:
    def __init__(self):
        self.letterlist=[0]*52;
        self.content=''
        self.filename='english.txt'
        self.sac=self.getasciifromchar('A')
        self.lac=self.getasciifromchar('a')
        self.dictofletter={}

    def readtext(self):
        f=open(self.filename)
        self.content=f.read()
    def getasciifromchar(self,letter):
        return ord(letter)
    def getcharfromascii(self,code):
        return chr(code)
    def count(self):
        for le in self.content:
            if le.isalpha():
                ac = self.getasciifromchar(le)
                if le.islower():
                    self.letterlist[ac-self.lac]=self.letterlist[ac-self.lac]+1
                else:
                    self.letterlist[ac-self.sac+26]=self.letterlist[ac-self.sac+26]+1
    def showmeans(self):
        le=0
        for x in self.letterlist:
            if le < 26:
                print self.getcharfromascii(le+self.lac),'\t',x
            else:
                print self.getcharfromascii(le-26+self.sac) ,'\t',x
            le=le+1
    def getditofletter(self):
        list1=string.letters
        self.dictofletter=zip(list1,self.letterlist)
        print self.dictofletter

c=countletter()
c.readtext()
c.count()
# c.showmeans()
c.getditofletter()