import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Authorization from "./Authorization"; 
import AllProducts from "./AllProducts";

function App() {
  return (
    <>
        <Routes>
          <Route path="/signup" element={<Authorization />}></Route>
          <Route path="/products" element={<AllProducts />}></Route>
        </Routes>
    </>
  )
}

export default App;