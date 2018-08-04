#coding=utf-8

from werkzeug import import_string, cached_property
from functools import wraps
from flask import request,render_template,session,current_app,url_for
from datetime import timedelta,datetime
from main.extensions import redis_store
from flask_sse import sse

from urllib.parse import urljoin
from urllib import parse
# from urlparse import urlparse, urljoin
import time


#延迟加载视图
class LazyView(object):

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)


def url(bp,url_rule, import_name, **options):
    view = LazyView('main.' + bp.name+'.views.'+ import_name)
    bp.add_url_rule(url_rule, view_func=view, **options)



#模板装饰器
def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator



"""http://flask.pocoo.org/snippets/71/
Counting Online Users with Redis
"""

def mark_online(user_id):
    now = int(time.time())
    expires = now + (current_app.config['ONLINE_LAST_MINUTES'] * 60) + 10
    all_users_key = 'online-users/%d' % (now // 60)
    user_key = 'user-activity/%s' % user_id
    p = redis_store.pipeline()
    p.sadd(all_users_key, user_id)
    p.set(user_key, now)
    p.expireat(all_users_key, expires)
    p.expireat(user_key, expires)
    p.execute()

def get_user_last_activity(user_id):
    last_active = redis_store.get('user-activity/%s' % user_id)
    if last_active is None:
        return None
    return datetime.utcfromtimestamp(int(last_active))

def get_online_users():
    current = int(time.time()) // 60
    minutes = range(current_app.config['ONLINE_LAST_MINUTES'])
    online_count = redis_store.sunion(['online-users/%d' % (current - x)
                         for x in minutes])
    
    return online_count


"""http://flask.pocoo.org/snippets/62/
Securely Redirect Back
"""

def is_safe_url(target):
    ref_url = parse(request.host_url)
    test_url = parse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target  

def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)

"""
    return redirect_back('index')
"""