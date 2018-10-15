#coding=utf-8
from main.helpers import url
from . import  bp

#home
url(bp,'/', 'home')
#logout
url(bp,'/logout/','logout')

#about
url(bp,'/about/','about')
#login
url(bp,'/login/','login',methods=['GET', 'POST'])

#图表测试
url(bp,'/home_json','home_json')

