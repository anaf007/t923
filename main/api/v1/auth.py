from flask import request



class Login(Resource=''):
    """用户登录."""
    def put(self):

        username = request.form['username']
        pwd = request.form['pwd']

        try:
            r = rocket.login(username,pwd)
        except Exception as e:
            r = None

        if not r:
            return {'state':'false'},401
  

        return {
            'status':state,
            'userId':userId,
            'authToken':authToken
        },200





