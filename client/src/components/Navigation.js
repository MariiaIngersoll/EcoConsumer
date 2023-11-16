import React from "react";
import { NavLink, Link } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { selectIsAuthenticated } from '../redux_store/AuthSlice';
import { logoutUser } from '../redux_store/AuthActions'
import Login from './Login';

import logoImage from "../GreenLogo.png"


function Navigation() {
  const isAuthenticated = useSelector(selectIsAuthenticated);
  const dispatch = useDispatch();

  const handleLogout = () => {
    // Dispatch the logout action
    dispatch(logoutUser());
  };

  return (
    <div className="nav-menu">
      <nav>
        <h2 className="logo">
          <span>
            <img src={logoImage} alt="Logo" className="logo-image" />
          </span>
          Eco<span>Consumer</span>
        </h2>
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
        {isAuthenticated ? (
          <>
            <button className="logoutBtn" type="button" onClick={handleLogout}>
              LOGOUT
            </button>
          </>
        ) : (
          <>
            <Link to="/login">
              <button className="loginBtn" type="button">
                LOGIN
              </button>
            </Link>
          </>
        )}
      </nav>
    </div>
  );
}

export default Navigation;