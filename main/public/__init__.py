# -*- coding: utf-8 -*-
"""The public module, including the homepage and user auth."""
from flask import Blueprint,session,request,make_response,current_app
from main.helpers import LazyView,mark_online,get_online_users
from flask_sse import sse

bp = Blueprint('public', __name__)

from . import routes,views  # noqa

import random,string
from datetime import datetime
try:
    from PIL import Image,ImageDraw,ImageFont,ImageFilter
except Exception as e:
    import Image,ImageDraw,ImageFont,ImageFilter
try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO

@bp.before_request
def before_request():
    #在线人数统计
    mark_online(request.remote_addr)
    #回话超时登出
    # session.permanent = True

    # sse.publish({"count": str(len(get_online_users()) if len(get_online_users()) > 0 else 0)}, type='online',channel='admin')


# 随机字母:
def rndChar():
    str = ''
    for i in range(4):
        str += chr(random.randint(65, 90))
    return str

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))




#验证码
@bp.route('/generate_verification_code')
def generate_verification_code():
    output = BytesIO()
    width = 70
    height = 30
    image = Image.new('RGB',(width,height),(255,255,255))
    #字体对象
    font = ImageFont.truetype(current_app.config['VERIFICATION_CODE_FONT'], 18)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    verify_str = rndChar() 

    draw.text((10, 5),verify_str, font=font, fill=rndColor2())

    #模糊
    # image = image.filter(ImageFilter.BLUR)
    # li = []
    # for i in range(10):
    #   temp = random.randrange(65,90)
    #   c = chr(temp)
    #   li.append(c)
    
    image.save(output,"JPEG")
    img_data = output.getvalue()
    session['verify'] = verify_str
    response = make_response(img_data)
    response.headers['Content-Type'] = 'image/jpeg'
    return response




