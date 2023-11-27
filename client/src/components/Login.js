import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { setUser } from '../redux_store/SessionSlice';
import { loginStart, loginSuccess, loginFailure } from '../redux_store/AuthSlice';

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const signInSchema = yup.object().shape({
    username: yup.string().required('Username is required'),
    password: yup.string().required('Password required'),
  });

  const handleSubmit = (values) => {
    dispatch(loginStart());
        fetch('http://127.0.0.1:5555/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(values),
        }).then((r) => {
            if (r.ok) {
                return r.json();
            } else {
                throw new Error('Oops something went wrong')
            }
        })
        .then((data) => {
            console.log('Data from server:', data);
            dispatch(loginSuccess(data));
            console.log('Data sent to setUser:', data);
            dispatch(setUser(data));  
            navigate('/');
        })
        .catch((error) => {
            console.error('Login failed:', error.message);
            dispatch(loginFailure(error.message));
        });
    };

  
  const signInFormik = useFormik({
    initialValues: {
        username: '',
        password: '',
    },
    validationSchema: signInSchema,
    onSubmit: handleSubmit,
  });
        
  return (
    <div className="centered-container">
      <form className="login-form" onSubmit={signInFormik.handleSubmit}>
        <input
          type="text"
          className="input-field"
          placeholder="Username"
          name="username"
          value={signInFormik.values.username}
          onChange={signInFormik.handleChange}
          onBlur={signInFormik.handleBlur}
        />
        {signInFormik.errors.username && signInFormik.touched.username && (
          <div className="error-message">{signInFormik.errors.username}</div>
        )}
  
        <input
          type="password"
          className="input-field"
          placeholder="Password"
          name="password"
          value={signInFormik.values.password}
          onChange={signInFormik.handleChange}
          onBlur={signInFormik.handleBlur}
        />
        {signInFormik.errors.password && signInFormik.touched.password && (
          <div className="error-message">{signInFormik.errors.password}</div>
        )}
  
        <button type="submit" className="login-button">Login</button>
      </form>
      
      <p>
        Don't have an account? <Link to="/signup" className="signup-link">Sign Up</Link>
      </p>
    </div>
  );

}

export default Login;