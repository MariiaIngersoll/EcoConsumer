import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Authorization from "./Authorization"; 
import AllProducts from "./AllProducts";
import Navigation from "./Navigation";
import Home from "./Home";
import AllCompanies from "./AllCompanies";
import SingleCompanyPage from "./SingleCompanyPage";
import SingleProductPage from "./SingleProductPage";

function App() {
  return (
    <>
      <Navigation />
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/signup" element={<Authorization />}></Route>
          <Route path="/products" element={<AllProducts />}></Route>
          <Route path="/companies" element={<AllCompanies />}></Route>
          <Route path="/companies/:companyId" element={ <SingleCompanyPage />} />
          <Route path="/products/:productId" element={ <SingleProductPage />} />
        </Routes>
    </>
  )
}

export default App;