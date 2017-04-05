#-*- coding:utf-8 -*-

import random
import string
class getacitivecode:
    def __init__(self):
        self.codelist=[]

    def random_char(self,y):
        return ''.join(random.choice(string.letters.replace('o','').replace('O','')+string.digits.replace('0','')) for x in range(y))
        # s=''
        # for x in range(1,y):
        #     s.join(random.choice(string.letters+string.digits))
        # return s

    def getcode(self,x=200,y=8):
        for i in range(x):
            s=self.random_char(y)
            self.codelist.append(s)

    def storelist(self):
        f= open('activitecode.txt','a+')
        # f.writelines(self.codelist)
        for l in self.codelist:
            f.write(l)
            f.write('\n')
    def showmelist(self):
        for l in self.codelist:
            print l

c=getacitivecode()
c.getcode()
c.storelist()
c.showmelist()