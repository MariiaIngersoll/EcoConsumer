import React, { useEffect, useState } from "react";
import SingleProductPage from "./SingleProductPage";
import { useSelector, useDispatch } from "react-redux";
import { setProducts } from "../redux_store/ProductsSlice";
import { useNavigate } from "react-router-dom";

function AllProducts() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.products.products);
  const navigate = useNavigate()

  const [searchQuery, setSearchQuery] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("All"); 

  const [filteredProducts, setFilteredProducts] = useState([]);

  
  useEffect(() => {
    fetch("http://127.0.0.1:5555/api/products")
      .then((r) => r.json())
      .then((data) => {
        dispatch(setProducts(data));
        setFilteredProducts(data); 
      });
  }, [dispatch]);

  
  const handleSearch = (e) => {
    const query = e.target.value;
    setSearchQuery(query);

    filterProducts(query, categoryFilter);
  };

  const handleCategoryFilter = (e) => {
    const category = e.target.value;
    setCategoryFilter(category);

    filterProducts(searchQuery, category);
  };

  const filterProducts = (query, category) => {
    let filtered = products;

    if (query) {
      filtered = filtered.filter((product) =>
        product.name.toLowerCase().includes(query.toLowerCase())
      );
    }

    if (category !== "All") {
      filtered = filtered.filter((product) => product.category === category);
    }

    setFilteredProducts(filtered);
  };

  const handleProductClick = (productId) => {
      navigate(`/products/${productId}`);
  }
  
  const productsArray = filteredProducts.map((product) => (
      <div
        className="single-product"
        key={product.id}
        onClick={() => handleProductClick(product.id)}
      >
      <img src={product.image}></img>
      <h1>{product.name}</h1>
      </div>
  ));

  const categories = Array.from(
    new Set(products.map((product) => product.category))
  );
  categories.unshift("All"); 

  return (
    <>
      <input
        type="text"
        placeholder="Search products by name..."
        value={searchQuery}
        onChange={handleSearch}
        className="search-bar"
      />
      <div className="filter-form">
        <label htmlFor="category">Filter by Category:</label>
        <select
          id="category"
          value={categoryFilter}
          onChange={handleCategoryFilter}
        >
          {categories.map((category) => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>
      <div className="products-container">
        {productsArray}
      </div>
    </>
  );
}

export default AllProducts;