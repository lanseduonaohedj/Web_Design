from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="afasdg"


# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/booktest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
# 初始化salalchemy
db = SQLAlchemy(app)



@app.route("/")
def intex():
    return "hello word"


if __name__ == '__main__':
    app.run(debug=True)