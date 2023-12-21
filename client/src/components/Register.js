import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import * as Yup from "yup";
import { loginStart, loginSuccess, loginFailure } from "../redux_store/AuthSlice";
import { setUser } from "../redux_store/SessionSlice";

function Register() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const validationSchema = Yup.object().shape({
    username: Yup.string().required("Username is required"),
    email: Yup.string().email("Invalid email").required("Email is required"),
    password: Yup.string()
      .min(6, "Password must be at least 6 characters")
      .required("Password is required"),
  });

  const handleSubmit = (values) => {
    dispatch(loginStart());
    fetch("/api/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(values),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Oops something went wrong');
        }
      })
      .then((data) => {
        dispatch(loginSuccess(data));
        dispatch(setUser(data))
        navigate('/')
      })
      .catch((error) => {
        dispatch(loginFailure(error.message));
      });
  };

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      image: "",
    },
    validationSchema: validationSchema,
    onSubmit: handleSubmit, 
  });

  return (
      <div className="signup-container">
        <h1>Register</h1>
        <form className="register-form" onSubmit={formik.handleSubmit}>
        <label htmlFor="image">IMAGE:</label>
        <input
          type="text"
          id="image"
          name="image"
          className="input-field"
          onChange={formik.handleChange}
          value={formik.values.image}
        />
  
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          name="username"
          className="input-field"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
        {formik.errors.username && formik.touched.username && (
          <div className="errors">{formik.errors.username}</div>
        )}
  
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          className="input-field"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
        {formik.errors.email && formik.touched.email && (
          <div className="errors">{formik.errors.email}</div>
        )}
  
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          className="input-field"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        {/* {formik.errors && (
          // <div className="errors">
          //   <ul>
          //     {Object.values(formik.errors).map((error, index) => (
          //       <h6 key={index}>{error}</h6>
          //     ))}
          //   </ul>
          // </div>
        )} */}
  
        <button type="submit" className="register-button">
          Register
        </button>
      </form>
  
      <p className="login-link">
      Already have an account? <Link to="/login">Login here.</Link>
     </p>
    </div>
  );
}

export default Register;