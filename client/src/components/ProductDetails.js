import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSingleProduct } from "../redux_store/ProductsSlice";
import { setReviewsForProduct, addReview } from "../redux_store/ReviewsSlice";
import { useParams } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function ProductDetails() {
  const { productId } = useParams();
  const [showForm, setShowForm] = useState(false);
  const dispatch = useDispatch();
  const singleProduct = useSelector((state) => state.products.singleProduct);
  const reviews = useSelector((state) => state.reviews.reviewsForProduct);

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/api/products/${productId}`)
      .then((r) => r.json())
      .then((data) => {
        dispatch(setSingleProduct(data));
        dispatch(setReviewsForProduct(data.reviews));
      });
  }, [dispatch, productId]);

  const handleAddReview = (values) => {
    return new Promise((resolve, reject) => {
      fetch("http://127.0.0.1:5555/api/reviews", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          content: values.content,
          rating: values.rating,
          user_id: 1, 
          product_id: productId,
        }),
      })
        .then((r) => r.json())
        .then((response) => {
          dispatch(addReview(response));
          resolve(); 
        })
        .catch((error) => {
          reject(error); 
        });
    });
  };

  const validationSchema = Yup.object().shape({
    rating: Yup.number()
      .typeError("Rating must be a number")
      .min(1, "Rating must be at least 1")
      .max(5, "Rating must be at most 5")
      .required("Rating is required"),
    content: Yup.string().required("Review content is required"),
  });

  return (
    <div className="single-product-page">
      <h1>{singleProduct.name}</h1>
      <h3>Manufacturer: {singleProduct?.manufacturer ? singleProduct.manufacturer.name : 'Unknown'}</h3>
      <img src={singleProduct?.image} alt={singleProduct?.name} />
      <div className="product-details">
        <h4>Category: {singleProduct?.category} </h4>
        <h4>Eco-Friendly Features: {singleProduct?.ecoFriendlyFeatures}</h4>
        <p>{singleProduct?.description}</p>
      </div>

      <div className="reviews">
        <h2>Reviews:</h2>
        {reviews.map((review) => (
          <div key={review.id} className="review">
            <p>Rating: {review.rating}</p>
            <p>{review.content}</p>
            {review.user ? (
              <p>By: {review.user.username}</p>
            ) : (
              <p>By: Unknown User</p>
            )}
          </div>
        ))}
<div className="review-form">
  <button onClick={() => setShowForm(true)}>Add Review</button>
  {showForm && (
    <Formik
      initialValues={{ rating: "", content: "" }} 
      validationSchema={validationSchema}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        handleAddReview(values).then(() => {
          resetForm();
          setSubmitting(false);
          setShowForm(false); 
        });
      }}
      enableReinitialize 
    >
      {({ isSubmitting }) => (
        <Form>
          <div>
            <Field type="number" name="rating" placeholder="Rating (1-5)" />
            <ErrorMessage name="rating" component="div" />
          </div>
          <div>
            <Field as="textarea" name="content" placeholder="Type your review here..." />
            <ErrorMessage name="content" component="div" />
          </div>
          <div>
            <button type="submit" disabled={isSubmitting}>
              Submit Review
            </button>
          </div>
        </Form>
      )}
    </Formik>
  )}
</div>
      </div>
    </div>
  );
}

export default ProductDetails;