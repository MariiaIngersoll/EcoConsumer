import { configureStore } from "@reduxjs/toolkit"
import  productsSlice  from "./ProductsSlice"
import  companiesSlice  from "./CompaniesSlice";
import  reviewsSlice  from "./ReviewsSlice";
import  authReducer from './AuthSlice';
import  sessionReducer from "./SessionSlice";

export const store = configureStore(
    {
        reducer: {
            products: productsSlice,
            companies: companiesSlice,
            reviews: reviewsSlice,
            auth: authReducer,
            session: sessionReducer,
        },
    }
);

