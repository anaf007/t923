from flask import (
    Blueprint, 
    flash, 
    redirect, 
    request, 
    url_for,
    current_app,
    session,
    make_response
)
from flask_login import login_required, login_user, logout_user,current_user
from main.forms.auth import LoginForm,RegisterForm
from main.tools.log import logger
from main.routes.auth import reg_url
from main.helpers import templated
from main.utils import flash_errors
bp = Blueprint('auth', __name__,url_prefix='/auth')
reg_url(bp)

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO
try:
    from PIL import Image,ImageDraw,ImageFont,ImageFilter
except Exception as e:
    import Image,ImageDraw,ImageFont,ImageFilter  

@templated()
def login():
    """login."""
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('登录成功.', 'success')
            logger.info('===ID:'+str(current_user.id)+'-login')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            form.verification_code.data = ''
            flash_errors(form)

    return dict(form=form)


@login_required
def logout():
    """退出登录."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@bp.route('/generate_verification_code')
def generate_verification_code():
    """验证码"""
    from main.tools.verification_code import rndChar,rndColor,rndColor2
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

    image.save(output,"JPEG")
    img_data = output.getvalue()
    session['verify'] = verify_str
    response = make_response(img_data)
    response.headers['Content-Type'] = 'image/jpeg'
    return response




