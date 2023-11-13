import React from "react";
import { NavLink } from "react-router-dom";
import logoImage from "../GreenLogo.png"
function Navigation() {
  return (
    <div className="nav-menu">
      <nav>
        <h2 className="logo">
        <span>
            <img src={logoImage} alt="Logo" className="logo-image"/> 
          </span>
          Eco<span>Consumer</span></h2>
        <ul>
          <li>
            <NavLink to="/">HOME</NavLink>
          </li>
          <li>
            <NavLink to="/products">PRODUCTS</NavLink>
          </li>
          <li>
            <NavLink to="/companies">COMPANIES</NavLink>
          </li>
        </ul>
        <button className="loginBtn" type="button">LOGIN</button>
      </nav>
    </div>
  );
}

export default Navigation;





