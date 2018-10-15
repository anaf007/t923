# -*- coding: utf-8 -*-
from main.helpers import url
from . import  bp

url(bp,'/', 'home')
#register
url(bp,'/add_users/','add_users',methods=['GET', 'POST'])