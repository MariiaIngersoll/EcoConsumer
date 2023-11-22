import React from "react";
import { NavLink, Link, useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { logout } from "../redux_store/AuthSlice";

import logoImage from "../GreenLogo.png"


function Navigation() {
  const dispatch = useDispatch();
  const navigate = useNavigate()

  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);

  function handleLogout() {
    fetch("http://127.0.0.1:5555/api/logout", {
        method: "DELETE"
    }).then((res) => {
        if (res.ok) {
            dispatch(logout());
            navigate("/")
        }
    });
}

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