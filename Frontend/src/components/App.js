import React, { Component } from 'react';
import './App.css';
import Navbar from  './Navbar';
import Consolas from './Consolas';

class App extends Component {
  render() {
    return (
      <div>
        <Navbar/>
        <Consolas/>
      </div>
      
    );
  }

}

export default App;
