from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help="video name", required=True)
video_put_args.add_argument('views', type=int, help="video views", required=True)
video_put_args.add_argument('views', type=int, help="video views", required=True)
video_put_args.add_argument('like', type=int, help="video likes", required=True)



class Video(Resource):
    def get(self, video_id):
        return {"Hello world"}
    
    def put(self,video_id):
        return{}
    

api.add_resource(Video,"/video/<int:video_id")

if __name__ =="main":
    app.run(debug=True)