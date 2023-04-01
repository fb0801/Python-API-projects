from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Model
import requests
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)
app.config["SQLAlCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.column(db.integer, primary_key=True)
    name  = db.column(db.string(100), nullable = False)
    views = db.column(db.integer, nullable = False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes = {likes})"


db.create_all()


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help="video name", required=True)
video_put_args.add_argument('views', type=int, help="video views", required=True)
video_put_args.add_argument('views', type=int, help="video views", required=True)
video_put_args.add_argument('like', type=int, help="video likes", required=True)
videos ={}

resource_feilds= {
    'id': fields.Integer,
    'name':fields.string,
    "views":fields.Integer,
    'likes':fields.Integer
}
class Video(Resource):
    @marshal_with(resource_feilds)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        return result
    
    @marshal_with(resource_feilds)
    def put(self,video_id):
        args= video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return videos[video_id]
    
    def delete(self, video_id):
        abort_video(video_id)
        del videos[video_id]
        return '',204

api.add_resource(Video,"/video/<int:video_id")

if __name__ =="main":
    app.run(debug=True)