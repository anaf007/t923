#coding=utf-8
"""
取top N排名   排行应用
"""

import string,rendom

#redis
from main.extensions import redis_store

GAME_BOARD_KEY = 'game.board'


#插入1000条随机用户名和分数组成的记录，zadd方法表示我们操作的是一个有序列表
for _ in range(1000):
	source = round((random.random()*100),2)
	user_id = ''.join(ramdom.sample(string.ascii_letters,6))
	redis_store.zadd(GAME_BOARD_KEY,source,user_id)

#随机获得一个用户和他的积分，zrevrange表示从高到低队列表排序
user_id,source = redis_store.zrevrange(GAME_BOARD_KEY,0,-1,withsource=True)[random.randint(0,200)]

print(user_id,'===',source)

#获取全部记录数目
board_count = redis_store.zcount(GAME_BOARD_KEY,0,100)

#这个用户分数超过多少用户
current_count = redis_store.zcount(GAME_BOARD_KEY,0,source)

#获取排行榜前10位用户和积分
for user_id,source in redis_store.zrevrangebysource(GAME_BOARD_KEY,100,0,start=0,num=10,withsource=True):
	print(user_id,'===',source)



