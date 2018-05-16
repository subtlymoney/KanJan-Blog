from flask import Flask
from config import DevConfig
import wt_forms

app = Flask(__name__)

# Import the views module
# views = __import__('views')
from views import *


# Get the config from object of DecConfig
# 使用config.from_object()，可以加载DecConfig类的变量配置集合
app.config.from_object(DevConfig)

# 在Jinja中自定义过滤器
# def count_substring_from_python(string, sub):
#     return string.count(sub)
# app.jinja_env.filters['count_substring'] = count_substring_from_python

if __name__ == '__main__':
    app.register_blueprint(blog_blueprint)
    # Entry the application
    app.run()