import Comment from "./Comment";
import Post from "../post/Post";

const CommentPage = ({ key, title, description, image, comments, likes}) => {
  return (
    <>
      <Post key={key} title={title} description={description} image={image}/>
      {comments.map((comment) => (
        <Comment
          key={comment.Comment_ID}
          user={comment.User_ID}
          comment={comment.Comment}
        />
      ))}
    </>
  );
};

export default CommentPage;
