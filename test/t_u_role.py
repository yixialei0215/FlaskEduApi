from mainapp import app
from models.user import User, Role, QX, user_role, db
from utils import crypt


def add_user():
    u1 = User()
    u1.phone = '17791692077'
    u1.auth_key = crypt.pwd('123456')
    u1.nick_name = 'Disen666@888'

    db.session.add(u1)
    print('保存数据之后的User-ID', u1.id)
    db.session.commit()
    print('提交之后', u1.id)

def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')

    # 批量添加
    db.session.add_all((r1, r2))
    db.session.commit()
    print(r1.id, r2.id)

def add_user_rol3():

    # db.Table()不能作为模型类使用
    # db.session.add_all((
    #     user_role(user_id=1,role_id=1),
    #     user_role(user_id=2,role_id=1),
    #     user_role(user_id=2,role_id=2)
    # ))
    # db.session.commit()
    # 为用户ID为1的用户增加“系统管理员角色”
    u = User.query.get(1)

    admin_role = Role.query.filter(Role.name.__eq__('系统管理员')).one()

    # 将角色对象添加给用户
    u.roles.append(admin_role)
    db.session.commit()
    print('ok')

def query_user_role(user_id=1):
    u = User.query.get(user_id)
    print('------当前用户的角色------')
    for role in u.roles:
        print(role.name)

if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)

    # add_role()
    # add_user_rol3()
    query_user_role(1)