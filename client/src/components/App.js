import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AllProducts from "./AllProducts";
import Navigation from "./Navigation";
import Home from "./Home";
import AllCompanies from "./AllCompanies";
import SingleCompanyPage from "./SingleCompanyPage";
import SingleProductPage from "./ProductDetails";
import Login from "./Login";
import Register from "./Register";

function App() {
  return (
    <>
      <Navigation />
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/login" element={<Login />}> </Route>
          <Route path="/signup" element={<Register />}> </Route>
          <Route path="/products" element={<AllProducts />}></Route>
          <Route path="/companies" element={<AllCompanies />}></Route>
          <Route path="/companies/:companyId" element={ <SingleCompanyPage />} />
          <Route path="/products/:productId" element={ <SingleProductPage />} />
        </Routes>
    </>
  )
}

export default App;