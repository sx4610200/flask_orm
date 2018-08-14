from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app) #实例化

class User (db.Model):
    _tablename_='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<User %r>'%self.name

@app.route('/get/',methods=['GET'])
def get_list():
    dict={}
    items=User.query.all()
    for ite in items:
           dict['items_name']=ite.name
           dict['id']=ite.id

    return jsonify(dict)


if __name__ == '__main__':

    app.run()
    print("=============")
