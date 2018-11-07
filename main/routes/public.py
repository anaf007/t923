#coding=utf-8
from main.helpers import url

def reg_url(bp):
    """注册路由"""
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
    #添加购物车
    url(bp,'/add_buy_car/<int:id>','add_buy_car')
