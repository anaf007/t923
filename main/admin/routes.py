#coding=utf-8
from main.helpers import url
from . import  bp

#admin主页
url(bp,'/', 'home')
url(bp,'/index/<string:name>', 'index')
#网站
url(bp,'/web_site', 'web_site')
#添加产品
url(bp,'/add_products', 'add_products',methods=['GET','POST'])
#所有用户
url(bp,'/all_users', 'all_users')

url(bp,'/all_products', 'all_products')

