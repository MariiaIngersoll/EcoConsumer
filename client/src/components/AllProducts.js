import React, { useEffect, useState } from "react";
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
    fetch("/api/products")
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
      <img src={product.image} alt={`Product: ${product.name}`} />
      <h1>{product.name}</h1>
      </div>
  ));

  const categories = Array.from(
    new Set(products.map((product) => product.category))
  );
  categories.unshift("All"); 

  return (
    <>
      <p className="paragraphForAllProducts">Explore our eco-conscious collection, a curated array of products designed to enhance your daily routine while being kind to the environment. From household essentials to body care favorites, each item aligns with our commitment to sustainability. They're not just products; they're eco-friendly solutions. Enjoy the journey of discovering and adding them to your favorites, taking steps towards a greener, more sustainable lifestyle.</p>
      <div className="filterAndSearchDiv">
      <label htmlFor="search">Search products by name:</label>
      <input
        type="text"
        placeholder="Start typing here..."
        value={searchQuery}
        onChange={handleSearch}
        className="search-bar"
        id="search"
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
      </div>
      <div className="products-container">
        {productsArray}
      </div>
    </>
  );
}

export default AllProducts;