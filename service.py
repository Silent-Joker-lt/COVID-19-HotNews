# -*- coding: utf-8 -*-
import pymysql
def open0():
    db = pymysql.connect("localhost", "root", "","丁香园国内",charset="utf8")
    return db
def open1():
    db = pymysql.connect("localhost", "root", "","丁香园国外",charset="utf8")
    return db
def open2():
    db = pymysql.connect("localhost", "root", "", "新闻", charset="utf8")
    return db
def query0(sql,*keys):
    db=open0()
    cursor = db.cursor()
    cursor.execute(sql,keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
def query1(sql,*keys):
    db=open1()
    cursor = db.cursor()
    cursor.execute(sql,keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
def query2(sql,*keys):
    db=open2()
    cursor = db.cursor()
    cursor.execute(sql,keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
#print(query0("select * from 重庆"))