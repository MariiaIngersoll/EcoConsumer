import { setUser, setToken, logout } from './AuthSlice';
import axios from 'axios';

export const loginUser = (credentials) => async (dispatch) => {
 
    const response = await axios.post('http://127.0.0.1:5555/api/login', credentials);
    dispatch(setUser(response.data.user));
    dispatch(setToken(response.data.token));
};

export const logoutUser = () => (dispatch) => {
  dispatch(logout());
};