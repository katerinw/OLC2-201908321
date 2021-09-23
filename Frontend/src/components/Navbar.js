import React, { Component } from 'react';
import './Navbar.css';
import './Reportes'

class Navbar extends Component {
    render() {
      return (
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <a class="navbar-brand" href="#">Proyecto2</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarColor02">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <button type="button" class="btn btn-secondary">Ejecutar</button>
              </li>
              <li class="nav-item">
                <button type="button" class="btn btn-secondary">Arbol AST</button>
              </li>
            </ul>
          </div >
        </nav >
      );
    }
  
  }
  
  export default Navbar;
  