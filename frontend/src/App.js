import logo from "./logo.svg";
import "./App.css";
import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import Login from "./components/login/login";

function App() {
  return (
    <div className="App">
      <Login />
    </div>
  );
}

export default App;
