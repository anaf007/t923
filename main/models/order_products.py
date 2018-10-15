#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime 

class OrderProduct(SurrogatePK, Model):
    """订单商品列表 快照

    列表参数：
     - name:名称
     - thumbnail：缩略图
     - 
     - 
     - 

    """

    __tablename__ = 'order_products'

    name = Column(db.String(100))
    thumbnail = Column(db.String(200))
    price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None),default=0)
    count = Column(db.Integer()) 


