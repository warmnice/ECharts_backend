from flask import render_template, jsonify
# .models只是models.py文件的示例名称
from .models import User, Post

def configure_routes(app):
    @app.route('/')
    def index():
        return 'Hello, World!'
    @app.route('/users', methods=['GET'])
    def get_users():
        # 查询数据库中的用户数据
        users = User.query.all()

        # 将用户数据传递给前端模板，可以使用 render_template 函数
        return render_template('users.html', users=users)

    @app.route('/posts')
    def get_posts():
        # 查询数据库中的帖子数据
        posts = Post.query.all()

        # 将帖子数据以 JSON 格式返回给前端
        return jsonify(posts=[post.serialize() for post in posts])
    
