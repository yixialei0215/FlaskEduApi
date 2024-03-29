from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Integer, String
from models import db

# 模型之间的关系不需要创建第三个模型类来实现第三张关系表的创建
# 创建用户和角色关系表
user_role = db.Table('user_role',
                     Column('user_id', Integer, ForeignKey('user.id', name='user_role_fk')),
                     Column('role_id', Integer, ForeignKey('role.id', name='user_role_pk')))
# role_table = db.Table('role_QX',
#                       Column('role_id',Integer,ForeignKey('role.id',name='role_table_fk')),
#                       Column('QX_id',Integer,ForeignKey('QX.id',name='role_table_pk')))

class BaseModel(db.Model):
    __abstract__ = True  # 作用：不会创建模型的对应的表
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)





class QX(BaseModel):
    __tablename__ = 'qx'

class Role(BaseModel):
    __tablename__ = 'role'
    # QXS = db.relationship(QX,secondary=role_table)

class User(db.Model):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    phone = Column(String(20),
                   unique=True,
                   nullable=False)
    auth_key = Column(String(100), nullable=False)
    nick_name = Column(String(20))
    photo = Column(String(100))

    # role_id = Column(ForeignKey('role.id'))
    # Many-to-Many 多对多关系，指定secondary设置关联的表，Table()
    roles = db.relationship(Role, secondary=user_role)
