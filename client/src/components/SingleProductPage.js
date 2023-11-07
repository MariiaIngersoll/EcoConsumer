import React from "react";

function SingleProductPage( {product} ) {

    return (
        <div className="single-product">
            <img src={product.image} alt={product.name} />
            <h1>{product.name}</h1>
        </div>
    )
}

export default SingleProductPage