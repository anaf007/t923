#coding=utf-8

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime as dt

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


class Products(SurrogatePK, Model):

    """产品列表 """    
    __tablename__ = 'products'

    name = Column(db.String(100))

    price = Column(db.Numeric(15,2))

    buys_id = relationship('ProductsBuys', backref='product')


class ProductsBuys(SurrogatePK, Model):
    """产品购买表"""

    __tablename__ = 'products_buys'

    users_id = reference_col('users')
    products_id = reference_col('products')
    #购买时间
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    



        
        