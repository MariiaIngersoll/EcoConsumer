import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import * as Yup from "yup";
import { loginStart, loginSuccess, loginFailure } from "../redux_store/AuthSlice";

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

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
    },
    validationSchema: validationSchema,
    onSubmit: async (values, { setSubmitting, setErrors }) => {
      try {
        dispatch(loginStart());

        const response = await fetch("http://127.0.0.1:5555/api/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        });

        if (response.ok) {
          const user = await response.json();
          dispatch(loginSuccess(user));
          navigate("/");
        } else {
          const error = await response.json();
          dispatch(
            loginFailure(error.message || "An unexpected error occurred.")
          );
        }
      } catch (error) {
        dispatch(
          loginFailure(error.message || "An unexpected error occurred.")
        );
      } finally {
        setSubmitting(false);
      }
    },
  });

  return (
    <div>
      <h1>Register</h1>
      <form onSubmit={formik.handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          name="username"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
        {formik.errors.username && formik.touched.username && (
          <div>{formik.errors.username}</div>
        )}

        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
        {formik.errors.email && formik.touched.email && (
          <div>{formik.errors.email}</div>
        )}

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        {formik.errors.password && formik.touched.password && (
          <div>{formik.errors.password}</div>
        )}

        <button type="submit">Register</button>
      </form>

      <Link to="/login">Already have an account? Login here.</Link>
    </div>
  );
}

export default Register;