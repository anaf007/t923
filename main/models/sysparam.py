#coding=utf-8

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship


class SysParam(SurrogatePK, Model):
    """系统参数表

    表名称：sysparam

    列表参数
     - web_name：站点名称
     - web_describe：站点描述
     - user_register：开放注册
     - active_site：是否启用站点
     - close_website_message:关闭站点提示消息
     - close_register_user_message:关闭会员注册提示消息
     - withdraw_money:允许提现

    """
    __tablename__ = 'sysconfig'
    web_name = Column(db.String(80),nullable=False)
    web_describe = Column(db.String(500))
    user_register = Column(db.Boolean,default=True)
    active_site = Column(db.Boolean,default=True)
    close_website_message = Column(db.String(500))
    close_register_user_message = Column(db.String(500))
    withdraw_money = Column(db.Boolean(),default=True)


    def init_insert():
        db.session.add(SysConfig(web_name='default'))
        db.session.commit()




