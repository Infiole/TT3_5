from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PostsModel(db.Model):
	Post_ID = db.Column(db.Integer, primary_key=True)
	Post_Title = db.Column(db.String(100))
	Post_Description = db.Column(db.String(100))
	Post_Image = db.Column(db.String(100))

	def __repr__(self):
		return f"posts(Post_ID = {Post_ID}, Post_Title = {Post_Title}, Post_Description = {Post_Description}, Post_Image = {Post_Image})"

# db.create_all()  # only call once to instantiate, if keep calling, overrides what we alr have
# db.session.commit()

# Posts = {1: ['Relatable', 'Walking up and down the aisles for what seems like hours.', 'https://preview.redd.it/jjvqtw9iapb81.gif?format=mp4&s=e333e78478df813b5b18ecd0905efc8b00ae210c'], 2: ['New Job', 'Just finished my first week', 'https://preview.redd.it/op4nak4pvpb81.jpg?width=640&crop=smart&auto=webp&s=615dce736df9a82ae1e2136727e440a863a1ffbe'], 3: ['New Friend', 'Happy times', 'https://preview.redd.it/21ghjyhnjmb81.gif?width=960&format=mp4&s=69ae3f05ee59793703165d1b726159dcc1205f1f'], 4: ['Gameboy', 'Hello old friend', 'https://i.redd.it/in0kdzuienb81.jpg'], 5: ['Dinosaur', 'Sweet dreams about your loved ones', 'https://preview.redd.it/rwtgu96btqb81.jpg?width=960&crop=smart&auto=webp&s=13b18d9fb9355b81349568a124955458f0f8d2e3'], 6: ['Sked penguin', 'SpoOOooOOoky', 'https://preview.redd.it/qcq4ktmgzqb81.jpg?width=960&crop=smart&auto=webp&s=52f3cd201555bf09534b903246df9cd0dd995264'], 7: ['Studying', 'Is this what its supposed to feel like?', 'https://i.redd.it/600fjw70hqb81.jpg'], 8: ['Mother', 'My mom sees no difference here', 'https://preview.redd.it/7m3h2v230qb81.jpg?width=640&crop=smart&auto=webp&s=9a6617330a192b1801c1af857233b28608d48b19'], 9: ['Buddy', 'You and me, we are friends now!', 'https://preview.redd.it/iwxtvicntqb81.gif?width=640&format=mp4&s=6cebc45c632020c2629dbf39be4492d55e6dce35'], 10: ['Love through Food', 'Buying food is a way to show love right.', 'https://preview.redd.it/n649wifg95041.jpg?width=960&crop=smart&auto=webp&s=0f6d7b4b57ce051d3d5a6ffce8a11e1ea0a5ebd9'], 11: ['Rhino', 'Less Threatening', 'https://preview.redd.it/tx6biuq81vb81.jpg?width=960&crop=smart&auto=webp&s=764d0e4b5c29d8abd36df97e842c817a10b9d1e8'], 12: ['Karaoke', 'Sing along time', 'https://i.redd.it/491l4somvtb81.jpg'], 13: ['Halo to Valo', 'Enough to make a grown man cry', 'https://preview.redd.it/e85me6m6fvb81.png?width=640&crop=smart&auto=webp&s=ca9622be8caf9cb187fdcb1ca15e6cdafd6ba2d6'], 14: ['Electrical Engineering', 'A wizard for sure', 'https://preview.redd.it/ii4eqom4xpa81.png?width=640&crop=smart&auto=webp&s=dc9af81b67c4113cd9d2bf1a6f1400b4028fd548'], 15: ['Christmas', 'A wholesome family', 'https://i.redd.it/xazlesb3c7981.jpg'], 16: ['Fashion', 'You are too hot!', 'https://preview.redd.it/4tfwjsvfxh881.jpg?width=960&crop=smart&auto=webp&s=7b4eddb5b50d03bf354ebeeda4f9aa90aa582d37'], 17: ['Listening Ear', 'I can do this all day', 'https://preview.redd.it/se55p3jvfd781.gif?format=mp4&s=261a874c2f4fbbc4383aa692b931531afdaf660f'], 18: ['Gaming', 'True hidden gems', 'https://preview.redd.it/mf1ud3kh3f881.gif?format=mp4&s=c7cb20547c4794a2d93e55053fcbbe041d7f6c44'], 19: ['Sushi', 'Amazing Chef', 'https://i.redd.it/q5wt8cj1jw881.jpg'], 20: ['Gym Bros', 'Fitness Goal', 'https://preview.redd.it/otu1l944db981.png?width=960&crop=smart&auto=webp&s=7edef7c548b567127e5be80de9ae24d1499d5ab3']}

# posts_to_add = db.session.query(Posts).all()
# for i in posts_to_add:
#     db.session.add(i)
# db.session.commit()

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

def abort_if_post_id_doesnt_exist(post_id):
    if post_id not in Posts:
        abort(404, message="Post id is not valid")


class Posts(Resource):
	#Return a list of all users’ posts from the Posts table
	@marshal_with(resource_fields)
	def get(self):
		result = PostsModel.query.all()
		return result

	#Insert the post created from frontend into the Posts table
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
	
	#Delete the user’s post from the Posts table
	def delete(self, post_id):
		abort_if_post_id_doesnt_exist(post_id)
		del post[post_id]
		return '', 204


api.add_resource(Posts, "/posts")

if __name__ == "__main__":
	app.run(debug=True)