import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Login from "./components/login/login";

function App() {
  return (
    <div className="App">
      <Login />
    </div>
  );
}

export default App;
