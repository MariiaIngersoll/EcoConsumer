import React, {useEffect, useState} from "react";
import SingleProductPage from "./SingleProductPage"
import { useSelector, useDispatch } from "react-redux"
import { setProducts  } from "../redux_store/ProductsSlice";

function AllProducts() {

    const dispatch = useDispatch()
    const products = useSelector((state) => state.products.products)

    useEffect( () => {
        fetch('http://127.0.0.1:5555/api/products')
        .then((r) => r.json())
        .then((products) => {
            dispatch(setProducts(products));
        })
    }, [dispatch]);

    const productsArray = products.map((product) => (
        <SingleProductPage product={product} key={product.id} />
    ));


    return (
        <div className="products-container">
            {productsArray}
        </div>
      );
    }

export default AllProducts;