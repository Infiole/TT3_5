import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Post from "./components/Post"
import Tweetbox from "./components/Tweetbox"
import Navbar2 from "./components/Navbar2"
import { Routes, Route, Link } from "react-router-dom";
import Section1 from "./components/Section1"
import Login from "./components/Login"

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Section1 />} />
        <Route path="/Logout" element={<Login />} />
      </Routes>
    </div>
  );
}

export default App;
