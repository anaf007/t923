#coding=utf-8

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship


class SysConfig(SurrogatePK, Model):
    """系统配置表 """
    __tablename__ = 'sysconfig'
    #站点名称
    web_name = Column(db.String(80),nullable=False)
    #站点描述
    web_describe = Column(db.String(500))
    #开放注册
    user_register = Column(db.Boolean,default=True)
    #是否启用站点
    active_site = Column(db.Boolean,default=True)


    def init_insert():
        db.session.add(SysConfig(web_name='default'))
        db.session.commit()

