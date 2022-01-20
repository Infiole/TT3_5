import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Login from "./components/login/login";
import Comment from "./components/feature/comment";

function App() {
  return (
    <div className="App">
      {/* <Login /> */}
      <Comment />
    </div>
  );
}

export default App;
