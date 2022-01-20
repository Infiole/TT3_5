from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
api = Api(app)
# read the database here INCLUDE THIS


class PostsModel(db.Model):
	Post_ID = db.Column(db.Integer, primary_key=True)
	Post_Title = db.Column(db.String(100))
	Post_Description = db.Column(db.String(100))
	Post_Image = db.Column(db.String(100))

	def __repr__(self):
		return f"posts(Post_ID = {Post_ID}, Post_Title = {Post_Title}, Post_Description = {Post_Description}, Post_Image = {Post_Image})"


posts_put_args = reqparse.RequestParser()
posts_put_args.add_argument(
    "Post_ID", type=int, help="Post_ID is required", required=True)
posts_put_args.add_argument("Post_Title", type=str,
                            help="Post_Title is required", required=True)
posts_put_args.add_argument(
    "Post_Description", type=str, help="Post_Description is required", required=True)
posts_put_args.add_argument("Post_Image", type=str,
                            help="Post_Image is required", required=True)

resource_fields = {
	'Post_ID': fields.Integer,
	'Post_Title': fields.String,
	'Post_Description': fields.String,
	'Post_Image': fields.String
}


class Posts(Resource):
	@marshal_with(resource_fields)
	def get(self):
		result = PostsModel.query.all()
		return result

	@marshal_with(resource_fields)
	def put(self, post_id):
		args = posts_put_args.parse_args()
		result = PostsModel.query.filter_by(Post_ID=post_id).first()
		if result:
			abort(409, message="Post id taken (must be unique)")

		post = PostsModel(Post_ID = post_id, post = args['Post_Title'], Post_Description = args['Post_Description'], Post_Image = args['Post_Image'])
		db.session.add(post)
		db.session.commit()
		return post, 201

api.add_resource(Posts, "/posts")

if __name__ == "__main__":
	app.run(debug=True)