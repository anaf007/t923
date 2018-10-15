#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime 

class Order(SurrogatePK, Model):
    """订单表：orders  

    列表参数：
     - users_id:外键用户表 购买人
     - products_id：外键产品表 产品id
     - created_at：创建时间
     - consignee:收货人
     - consignee_phone:收货人电话
     - consignee_adress:收货人地址
     - count:购买总数量
     - price：总金额
     - pay_type:支付类型  
     - buy_type:购买类型 
     - state:订单状态 默认0

    """

    __tablename__ = 'orders'

    users_id = reference_col('users')
    products_id = reference_col('products')
    
    consignee = Column(db.String(30))
    consignee_phone = Column(db.String(30))
    consignee_address = Column(db.String(200))
    count = Column(db.Integer())
    price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None),default=0)
    pay_type = Column(db.String(100))
    buy_type = Column(db.String(100))
    state = Column(db.Integer(),default=0)
    created_at = Column(db.DateTime, nullable=False, 
        default=datetime.datetime.now)


