#coding=utf-8
from main.helpers import url

def reg_url(bp):
    url(bp,'/login', 'login',methods=['GET','POST'])
    url(bp,'/logout', 'logout')