#coding=utf-8
#users用户模块路由


from main.helpers import url

def reg_url(bp):
    """注册路由"""

    url(bp,'/', 'home')
    url(bp,'/buys_car', 'buys_car')
    url(bp,'/submit_order', 'submit_order',methods=['GET', 'POST'])