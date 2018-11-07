#coding=utf-8

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
 
from .orders import Order
import datetime

class Product(SurrogatePK, Model):

    """产品列表 :products

    列表参数：
     - name：产品名称
     - price：销售价
     - special_price：优惠价进货价
     - note：详情
     - attach_key:附加字段
     - attach_value:附加值
     - active:商品状态
     - is_sell:是否出售
     - order_id：外键订单表
     - category_id：外键分类

    """    
    __tablename__ = 'products'

    category_id = reference_col('categorys')

    name = Column(db.String(100))
    price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None))
    special_price = Column(db.Numeric(precision=10,scale=2,\
        asdecimal=True, decimal_return_scale=None))
    note =  Column(db.UnicodeText())
    attach_key = Column(db.String(500))
    attach_value = Column(db.String(500))
    active = Column(db.Boolean(),default=True)
    is_sell = Column(db.Boolean(),default=True)
    #热门 0 不热门 1热门
    hot = Column(db.Boolean(),default=True)
    #查看次数
    click_count = Column(db.Integer(),default=0)
    #累计购买总数
    buy_count = Column(db.Integer(),default=0)
    #条码
    ean = Column(db.String(50))
    #规格
    unit = Column(db.Integer,default=1)
    #创建时间
    created_at = Column(db.DateTime, default=datetime.datetime.now)
    #首页展示图
    main_photo = Column(db.String(200))


    def get_all(self):
        return Product.query.all()



class Category(SurrogatePK,Model):
    """产品分类表：categorys  

    列表参数：
     - product_id:外键产品表 产品id
     - name:分类名称
     - ico：分类图标
     - sort：分类排序
     - active：是否激活 用户是否删除？
     - show：是否显示  
     
    """

    __tablename__ = 'categorys'

    name = Column(db.String(100))
    ico = Column(db.String(200))
    sort = Column(db.Integer())
    active = Column(db.Boolean(),default=True)
    show = Column(db.Boolean(),default=True)


    #:自身上级，引用自身无限级分类
    parent = reference_col('categorys')
    childrens = relationship("Category",lazy="joined",join_depth=2)
    
    product_id = relationship(Product, backref='products')



    



