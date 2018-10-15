#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime 

class Store(SurrogatePK,Model):
    """店铺 stores

    列表参数：
     - users_id：外键用户表
     - name:店铺名称
     - created_at：创建时间
     - active：是否激活。默认false

    """
    __tablename__ = 'stores'

    users_id = reference_col('users')

    name = Column(db.String(100))
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    active = Column(db.Boolean(), default=False)








