#coding=utf-8
from main.extensions import sse
from time import sleep
from main.helpers import get_online_users
import psutil

def publish_cpu(app,flag=True):
    try:
        print(app)
    
        with app.app_context():
            while flag:
                sse.publish({"cpu_use":psutil.cpu_percent()}, type='cpu_use',channel='admin')
                sleep(10)

    except Exception as e:
        print(str(e))


def onlinr_users(app,flag=True):
    with app.app_context():
        while flag:
            sse.publish({"count": str(len(get_online_users()) if len(get_online_users()) > 0 else 0)}, type='online',channel='admin')
            sleep(10)
