from peewee import *
import pymysql
import datetime

db = MySQLDatabase('db', user='root', password='Om19ha17ar&',
                         host="localhost", port=3306)

class company(Model):
    deprtamen=CharField()
    position=CharField(null=False)
    namec=CharField(null=False)
    Email=CharField(null=False,unique=True)
    class Meta:
        database = db



class employ(Model):

    name=CharField(null=False)
    depratment=ForeignKeyField(company , backref='deprtamen')
    position=ForeignKeyField(company , backref='company')
    bdate=DateField(null=False)
    jdate=DateField(null=False)
    salary=IntegerField(null=False)
    geneder=CharField(null=False)
    image=CharField(null=False)
    email=CharField(null=False,unique=True)
    address=CharField(null=False)
    pnumber=IntegerField(null=False,unique=True)
    class Meta:
        database = db
chose=(
    (1,'here'),
    (2,'not here')
)
class dailymovement(Model):
    ename=ForeignKeyField(employ,backref='event')
    edepartment=ForeignKeyField(employ,backref='event')
    eposition=ForeignKeyField(employ, backref='event')
    state=CharField(choices=chose)
    datet=DateTimeField(datetime.datetime.now)
    salaryc=IntegerField()
    class Meta:
        database = db   
class monthelymovement(Model):
    ename=ForeignKeyField(employ,backref='event')
    edepartment=ForeignKeyField(employ,backref='event')
    eposition=ForeignKeyField(employ, backref='event')
    datet=ForeignKeyField(dailymovement,backref='datet')
    salary=ForeignKeyField(employ,backref='salary')
    daily=ForeignKeyField(dailymovement,backref='daily')
    salaryc=IntegerField()
    class Meta:
        database = db


class monthlyemlpoy(Model):
    ename=ForeignKeyField(employ,backref='event')
    edepartment=ForeignKeyField(employ,backref='event')
    eposition=ForeignKeyField(employ, backref='event')
    datet=ForeignKeyField(dailymovement,backref='datet')
    salary=ForeignKeyField(employ,backref='salary')
    daily=IntegerField()
    salaryc=IntegerField()
    class Meta:
        database = db

class users(Model):
    name=CharField(null=False, unique=True)
    password=CharField(null=False , unique=True)
    class Meta:
        database = db


db.connect()
db.create_tables([company,users,employ,dailymovement,monthelymovement,monthlyemlpoy])