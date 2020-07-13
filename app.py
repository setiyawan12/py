from flask import Flask, Response, json, jsonify, request, abort
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/kampus'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/admin/')
def adminpage():
    return 'ini panel admin'


class HelloWorld(Resource):
    def get(self):
        return {'setiyawan': 'setiyawan'}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def get_all_users():
        return User.all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email')


api.add_resource(HelloWorld, '/helloworld')

if __name__ == '__main__':
    app.run()
