#coding=utf-8
from main.helpers import url

def reg_url(bp):
    url(bp,'/', 'home')
    #register
    url(bp,'/add_users/','add_users',methods=['GET', 'POST'])