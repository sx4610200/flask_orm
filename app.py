from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)  # 实例化


class User(db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.name



#查
@app.route('/get/', methods=['GET'])
def get_list():

    list = []
    items = User.query.all()
    print(items)
    for ite in items:
        dict = {}
        dict['items_name'] = ite.name
        dict['id'] = ite.id
        list.append(dict)
        print(list)
    return jsonify({'result': list})

#查
@app.route('/get/<int:uid>', methods=['GET'])
def getuid_list(uid):
    items = User.query.filter_by(id=uid).first()
    print(items)
    id = items.id
    name = items.name
    dict={}
    dict['id'] = id
    dict['name'] = name
    return jsonify({'result': dict})

#改(更新)
@app.route('/put/<int:uid>', methods=['PUT'])
def put_list(uid):
    print(uid)
    item = User.query.filter_by(id=uid).first()
    item.id = request.json.get('id')
    item.name = request.json.get('name')
    dict={}
    dict['id'] = item.id
    dict['name'] = item.name
    return jsonify({'result': dict})




if __name__ == '__main__':
    # db.create_all()
    print("=============")
    app.run()
