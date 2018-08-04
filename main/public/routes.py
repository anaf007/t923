#coding-utf-8
from main.helpers import url
from . import  bp

#home
url(bp,'/', 'home')
#logout
url(bp,'/logout/','logout')
#register
url(bp,'/register/','register',methods=['GET', 'POST'])
#about
url(bp,'/about/','about')
#login
url(bp,'/login/','login',methods=['GET', 'POST'])

