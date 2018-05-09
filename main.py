from flask import Flask
from config import DevConfig

app = Flask(__name__)

# Import the views module
views = __import__('views')

# Get the config from object of DecConfig
# 使用config.from_object()，可以加载DecConfig类的变量配置集合
app.config.from_object(DevConfig)



if __name__ == '__main__':
    # Entry the application
    app.run()