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
    <div>
      <form onSubmit={signInFormik.handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          name="username"
          value={signInFormik.values.username}
          onChange={signInFormik.handleChange}
          onBlur={signInFormik.handleBlur}
        />
        {signInFormik.errors.username && signInFormik.touched.username && (
          <div>{signInFormik.errors.username}</div>
        )}

        <input
          type="password"
          placeholder="Password"
          name="password"
          value={signInFormik.values.password}
          onChange={signInFormik.handleChange}
          onBlur={signInFormik.handleBlur}
        />
        {signInFormik.errors.password && signInFormik.touched.password && (
          <div>{signInFormik.errors.password}</div>
        )}

        <button type="submit">Login</button>
      </form>
      <p>
        Don't have an account? <Link to="/signup">Sign Up</Link>
      </p>
    </div>
  )
};

export default Login;