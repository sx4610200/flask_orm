from flask import Flask, request, jsonify,make_response
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

#使404变成更好看的json格式
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

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
    db.session.add(item)
    db.session.commit()
    return jsonify({'result': 'success'})

#创建(插入)
@app.route('/post/', methods=['POST'])
def post_list():
    new_dict = User(name=request.json['name'])
    print(new_dict)
    print(new_dict.id)
    print(new_dict.name)
    db.session.add(new_dict)
    db.session.commit()
    return jsonify({'result': 'add success'})

@app.route('/delete/<int:uid>',methods=['DELETE'])
def delete_list(uid):
    item=User.query.filter_by(id=uid).first()
    db.session.delete(item)
    db.session.commit()
    return "delete success"

if __name__ == '__main__':
    # db.create_all()
    print("=============")
    app.run()
