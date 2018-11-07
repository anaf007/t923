
import random,string
from datetime import datetime



from ..views.public import bp as public_bp


def rndChar():
    """随机字母:"""
    str = ''
    for i in range(4):
        str += chr(random.randint(65, 90))
    return str


def rndColor():
    """随机颜色1"""
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    """随机颜色2"""
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


@public_bp.route('/generate_verification_code')
def generate_verification_code():
    """验证码"""
    
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




