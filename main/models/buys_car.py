#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime 



class BuysCar(SurrogatePK, Model):
	"""购物车
	参数列表：
	 - add_price：添加时的价格
	 - product_id:产品id，不做外键
	 - count：数量

	"""

	__tablename__ = 'buys_car'

	add_price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None),default=0)

	product_id = Column(db.Integer())
	count = Column(db.Integer()) 

	users_id = reference_col('users')




