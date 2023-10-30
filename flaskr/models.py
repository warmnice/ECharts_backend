from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# 模型的字段与数据库表中的列相对应，以及他们的数据类型和约束

# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# 帖子模型
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=db.func.now(), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)

    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __init__(self, author_id, title, body):
        self.author_id = author_id
        self.title = title
        self.body = body