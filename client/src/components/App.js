import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Authorization from "./Authorization"; 
import AllProducts from "./AllProducts";
import Navigation from "./Navigation";
import Home from "./Home";
import AllCompanies from "./AllCompanies";

function App() {
  return (
    <>
      <Navigation />
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/signup" element={<Authorization />}></Route>
          <Route path="/products" element={<AllProducts />}></Route>
          <Route path="/companies" element={<AllCompanies />}></Route>
        </Routes>
    </>
  )
}

export default App;