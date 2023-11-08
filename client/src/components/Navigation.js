import React from "react";
import { NavLink } from "react-router-dom";

function Navigation() {
  return (
    <div className="nav-menu">
      <nav>
        <h2 className="logo">Eco<span>Consumer</span></h2>
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
        <button className="loginBtn" type="button">Login</button>
      </nav>
    </div>
  );
}

export default Navigation;





