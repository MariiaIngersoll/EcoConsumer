import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { setSingleProduct } from "../redux_store/ProductsSlice";
import { setReviewsForProduct, addReview, updateReview , deleteReview} from "../redux_store/ReviewsSlice";
import { useParams } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function ProductDetails({ user, isAuthenticated }) {
  const { productId } = useParams();
  const [showForm, setShowForm] = useState(false);
  const [editReview, setEditReview] = useState(null);
  const dispatch = useDispatch();
  const singleProduct = useSelector((state) => state.products.singleProduct);
  const reviews = useSelector((state) => state.reviews.reviewsForProduct);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await fetch(`/api/products/${productId}`);
        if (!response.ok) {
          throw new Error("Failed to fetch product");
        }
        const data = await response.json();
        dispatch(setSingleProduct(data));
        dispatch(setReviewsForProduct(data.reviews));
      } catch (error) {
        console.error("Error fetching product:", error);
      }
    };
    fetchProduct();
  }, [dispatch, productId]);

  const handleAddReview = async (values) => {
    try {
      const response = await fetch("/api/reviews", {
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
      });

      if (!response.ok) {
        throw new Error("Failed to add review");
      }
      const newReview = await response.json();
      dispatch(addReview(newReview));
    } catch (error) {
      console.error("Error adding review:", error);
    }
  };

  const handleEditClick = (reviewId) => {
    const reviewToEdit = reviews.find((r) => r.id === reviewId);
    setEditReview(reviewToEdit);
    console.log('Updated editReview state:', editReview);
    setShowForm(true);
  };

  const handleUpdateReview = async (values) => {
    const response = await fetch(`/api/products/${productId}/reviews/${editReview.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        rating: values.rating,
        content: values.content,
      }),
    });
    if (!response.ok) {
      throw new Error("Failed to update review! :(");
    }
    const updatedReview = await response.json();
    dispatch(updateReview(updatedReview));
    setEditReview(false);
    setShowForm(false);
  };

  const handleDeleteClick = (deletedId) => {
    console.log(`DELETED: ID ${deletedId}`)
  }

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
      {singleProduct.manufacturer ? (
      <h3>Manufacturer: {singleProduct.manufacturer.name}</h3>
    ) : (
      <h3>Manufacturer: Unknown</h3>
     )}
      <img src={singleProduct?.image} alt={singleProduct?.name} />
      <div className="product-details">
        <h4>Category: {singleProduct?.category} </h4>
        <h4>Eco-Friendly Features: {singleProduct?.ecoFriendlyFeatures}</h4>
        <p>{singleProduct?.description}</p>
      </div>

    <div className="reviews">
      <h2>Reviews:</h2>
      {reviews.map((review) => (
        <div key={review.id}  className="review" >
          <p >Rating: {review.rating}</p>
          <p>{review.content}</p>
          <p>By: {review.user.username}</p>
          {isAuthenticated && user.id === review.user.id && (
            <>
              <button onClick={() => handleEditClick(review.id)}>Edit Comment</button>
              <button onClick={() => handleDeleteClick(review.id)}>DELETE</button>
            </>
          )}
        </div>
      ))}
        
      {isAuthenticated? 
      <div className="review-form">
      <button onClick={() => setShowForm(true)}>Add Review</button>
      {showForm && (
        <Formik
          initialValues={{
            rating: editReview ? editReview.rating : "",
            content: editReview ? editReview.content : "",
          }}
          validationSchema={validationSchema}
          onSubmit={(values, { setSubmitting, resetForm }) => {
            if (editReview) {
              handleUpdateReview(values);
            } else {
              handleAddReview(values);
            }
            resetForm();
            setSubmitting(false);
            setShowForm(false);
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