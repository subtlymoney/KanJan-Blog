from flask import Flask, redirect, url_for
# from config import DevConfig
from KanJanBlog.config import DevConfig
from KanJanBlog.controllers import blog
from KanJanBlog.models import db

app = Flask(__name__)

# Import the views module
# views = __import__('views')
# from views import *

# Get the config from object of DecConfig
# 使用config.from_object()，可以加载DecConfig类的变量配置集合
app.config.from_object(DevConfig)

# Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
db.init_app(app)

# 在Jinja中自定义过滤器
# def count_substring_from_python(string, sub):
#     return string.count(sub)
# app.jinja_env.filters['count_substring'] = count_substring_from_python

@app.route('/')
def index():
    # Redirect the Request_url '/' to '/blog/'
    return redirect(url_for('blog.home'))

# Register the Blueprint into app object
app.register_blueprint(blog.blog_blueprint)

if __name__ == '__main__':
    # Entry the application
    app.run()