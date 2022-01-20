import { useParams, Link } from "react-router-dom";
import Post from "./Post";

const Posts = ({ posts, commentNumber, likeNumber }) => {
  return (
    <>
      {posts.map((post) => (
        <Post
          id={post.id}
          title={post.title}
          description={post.description}
          image={post.image}
          commentNumber={commentNumber}
          likeNumber={likeNumber}
          posts = {posts}
        />
      ))}
    </>
  );
};

export default Posts;
