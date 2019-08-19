from flask import render_template
from flask_script import Manager

from mainapp import app
from mainapp.views import user_v
from models.user import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_db')
def create_databases():
    db.create_all()
    return '创建数据库中的所有模型表成功'

@app.route('/drop_db')
def drop_databases():
    db.drop_all()
    return '删除数据库中的所有模型表成功'

if __name__ == '__main__':

    # 将蓝图注册
    app.register_blueprint(user_v.blue,url_prefix='/user')

    # 初始化db
    db.init_app(app)

    manager = Manager(app)
    manager.run()
