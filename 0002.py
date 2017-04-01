# -*- coding:utf-8 -*-

import MySQLdb

class connectdb:

    def __init__(self):
        self.url='localhost'
        self.username='root'
        self.password=''
        self.dbname='python'
        self.codelist=[]
        self.db = MySQLdb.connect(self.url, self.username, self.password, self.dbname)

    def getlist(self):
        f=open("activitecode.txt")
        while 1:
            l=f.readline()
            self.codelist.append(l)
            if not l:
                break

    def insert(self):
        cursor = self.db.cursor()
        sql="insert into activitycode(code) values("
        for l in self.codelist:
            sql=sql+'\''+l+'\''+')'
            print sql
            try:
                cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
        self.db.close();

p=connectdb()
p.getlist()
p.insert()