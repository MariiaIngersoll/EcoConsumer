import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSingleProduct} from "../redux_store/ProductsSlice";
import { useParams } from "react-router-dom";
import AddReviewButton from "./AddReviewButton";

function SingleProductPage() {
  const { productId } = useParams();
  const dispatch = useDispatch();

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/api/products/${productId}`)
      .then((r) => r.json())
      .then((data) => {
        console.log(data)
        dispatch(setSingleProduct(data)); 
      });
  }, [dispatch, productId]);

  console.log(productId)
  const singleProduct = useSelector((state) => state.products.singleProduct);

  console.log(singleProduct)

  if (!singleProduct) {
    return <div>Loading...</div>;
  }

  return (
    <div className="single-product-page">
      <h1>{singleProduct.name}</h1>
      <h3>Manufacturer: {singleProduct.manufacturer.name}</h3>
      <img src={singleProduct.image} alt={singleProduct.name} />
      <div className="descriptionProduct">
      <h4>Category: {singleProduct.category} </h4>
      <h4>Eco-Friendly Features: {singleProduct.ecoFriendlyFeatures}</h4>
      <p>{singleProduct.description}</p>
      </div>
      
      <div className="reviews">
        <h2>Reviews:</h2>
        {singleProduct.reviews.map((review) => (
        <div key={review.id} className="review">
            <p>Rating: {review.rating}</p>
            <p>Review: {review.content}</p>
            {review.user ? (
            <p>By: {review.user.username}</p>
            ) : (
            <p>By: Unknown User</p>
            )}
        </div>
        ))}
        <AddReviewButton />
      </div>
    </div>
  );
}

export default SingleProductPage