import './App.css';
import React, { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import api from "./api/backend.js"
import Login from "./components/login/login"
import Register from "./components/register/Register"
import Posts from "./components/post/Posts"
import CommentPage from './components/comment/CommentPage';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  const [posts, setPosts] = useState([])
  const [likes , setLikes] = useState([])

  const [comments, setComments] = useState('');

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get('/post');
        setPosts(response.data);
      } catch (err) {
        console.log(`Error: ${err.message}`);
      }
    }
    fetchPosts();
  }, [])

  useEffect(() => {
    const fetchLikes = async () => {
      try {
        const response = await api.get('/liked_post');
        setLikes(response.data);
      } catch (err) {
        console.log(`Error: ${err.message}`);
      }
    }
    fetchLikes();
  }, [])

  useEffect(() => {
    const fetchComments = async () => {
      try {
        const response = await api.get('/comments');
        setComments(response.data);
      } catch (err) {
        console.log(`Error: ${err.message}`);
      }
    }
    fetchComments();
  }, [])

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/"
            element={<Posts posts={posts} likes={likes} comments={comments}/>}
            />
          <Route path="/login"
            element={<Login/>}/>
          <Route path="/register"
          element={<Register/>}/>
          <Route path="/post"
            element={<CommentPage />}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
