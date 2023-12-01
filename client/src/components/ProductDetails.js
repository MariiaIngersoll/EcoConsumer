import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useNavigate } from "react-router-dom"; 
import { setSingleProduct } from "../redux_store/ProductsSlice";
import { setReviewsForProduct, addReview } from "../redux_store/ReviewsSlice";
import { useParams } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function ProductDetails( {user, isAuthenticated } ) {
  const { productId } = useParams();
  const [showForm, setShowForm] = useState(false);
  const dispatch = useDispatch();
  const singleProduct = useSelector((state) => state.products.singleProduct);
  const reviews = useSelector((state) => state.reviews.reviewsForProduct);

  const navigate = useNavigate()

  useEffect(() => {
    fetch(`/api/products/${productId}`)
      .then((r) => {
        if (!r.ok) {
          throw new Error('Failed to fetch product');
        }
        return r.json();
      })
      .then((data) => {
        dispatch(setSingleProduct(data));
        dispatch(setReviewsForProduct(data.reviews));
      })
      .catch((error) => {
        console.error('Error fetching product:', error);
        // Handle the error, e.g., show an error message to the user
      });
  }, [dispatch, productId]);

  const handleAddReview = (values) => {
    return new Promise((resolve, reject) => {
      fetch("/api/reviews", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          content: values.content,
          rating: values.rating,
          user_id: user.id, 
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
            <p>By: {review.user.username}</p>
          </div>
        ))}
    {isAuthenticated? 
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
          >
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
              <button type="submit" >
                Submit Review
              </button>
            </div>
          </Form> 
      </Formik>
    )}
   </div> : (
      <div>
      <h3>LOGIN TO ADD A COMMENT</h3>
      <p>
        Already have an account? <Link to={`/login?redirect=${window.location.pathname}`}>LOGIN HERE</Link>
      </p>
    </div>)}

      </div>
    </div>
  );
}

export default ProductDetails;