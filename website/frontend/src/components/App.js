import React, { Component } from "react";
import { render } from "react-dom";

import logo from '../../static/images/logo.svg';

console.log(logo);

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);