#coding=utf-8

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
 
from .orders import Order

class Product(SurrogatePK, Model):

    """产品列表 :products

    列表参数：
     - name：产品名称
     - price：价格
     - order_id：外键订单表

    """    
    __tablename__ = 'products'

    name = Column(db.String(100))
    thumbnail = Column(db.String(200))
    price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None),default=0)

    order_id = relationship(Order, backref='products')



