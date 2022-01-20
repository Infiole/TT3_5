import { useParams, Link } from "react-router-dom";
import Post from "./Post";

const Posts = ({ posts, likes, comments }) => {
  return (
    <>
      {posts.map((post) => (
        <Post
          key={post.Post_ID}
          title={post.Post_Title}
          description={post.Post_Description}
          image={post.Post_image}
        />
      ))}
    </>
  );
};

export default Posts;
