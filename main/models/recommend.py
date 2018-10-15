#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
import datetime

class Recommend(SurrogatePK,Model):
    """用户推荐表.recommend
    
    列表参数：

    """
    __tablename__ = 'recommend'
    #推荐人
        # recommend_id = reference_col('users.id')
        # #被推荐人
        # recommender_id = reference_col('users.id')
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    #被推荐人
    recommender_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        primary_key=True)
    #推荐人
    recommends_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        primary_key=True)


