from flask import Blueprint, request, render_template

blue = Blueprint('userBlue',__name__)

@blue.route('/user',methods=['GET','POST'])
def login():
    data = {
        'cookies':request.cookies,
        'base_url':request.host_url
    }
    return render_template('user/user.html',**data)