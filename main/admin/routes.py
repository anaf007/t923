#coding=utf-8
from main.helpers import url
from . import  bp

#home
url(bp,'/', 'home')
url(bp,'/index/<string:name>', 'index')
url(bp,'/web_site', 'web_site')
