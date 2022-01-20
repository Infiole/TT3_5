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
          likes={likes}
          comments={comments}
        />
      ))}
    </>
  );
};

export default Posts;
