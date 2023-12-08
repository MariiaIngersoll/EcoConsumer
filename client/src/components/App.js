import React, {useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { setUser } from "../redux_store/SessionSlice";
import { loginSuccess, logout } from "../redux_store/AuthSlice";

import AllProducts from "./AllProducts";
import Navigation from "./Navigation";
import Home from "./Home";
import AllCompanies from "./AllCompanies";
import SingleCompanyPage from "./SingleCompanyPage";
import SingleProductPage from "./ProductDetails";
import Login from "./Login";
import Register from "./Register";

function App() {

  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();
  const user = useSelector((state) => state.auth.user)

  console.log(user)
  useEffect(() => {
    fetch("/api/check_session").then((res) => {
      if (res.ok){
        res.json().then((userData) => {
          dispatch(setUser(userData)); 
          dispatch(loginSuccess(userData)); 
        });
      } else {
        dispatch(logout()); 
      }
    });
  }, [dispatch]);
  


  return (
    <>
      <Navigation />
        <Routes>
          <Route path="/" element={<Home isAuthenticated={isAuthenticated} />}></Route>
          <Route path="/login" element={<Login />}> </Route>
          <Route path="/signup" element={<Register />}> </Route>
          <Route path="/products" element={<AllProducts />}></Route>
          <Route path="/companies" element={<AllCompanies />}></Route>
          <Route path="/companies/:companyId" element={ <SingleCompanyPage />} />
          <Route path="/products/:productId" element={ <SingleProductPage user={user} isAuthenticated={isAuthenticated} />} />
        </Routes>
        <div className="footer">
        <div className="social-icons">
            <a href="#" target="_blank">Facebook</a>
            <a href="#" target="_blank">Twitter</a>
            <a href="#" target="_blank">Instagram</a>
        </div>
        <div>
            <a href="#">About Us</a>
            <a href="#">Contact Us</a>
            <a href="#">Privacy Policy</a>
        </div>
        <div className="copyright">
            &copy; 2023 Your Website. All rights reserved.
        </div>
        </div>
        
    </>
  )
}

export default App;