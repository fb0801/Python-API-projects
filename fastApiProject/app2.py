from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from requests import request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HellowWorld(Resource):
    def get(self, name, test):
        return {"Hello world"}
    

api.add_resource(HellowWorld,"/")

if __name__ =="main":
    app.run(debug=True)