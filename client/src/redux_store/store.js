import { configureStore } from "@reduxjs/toolkit"
import { productsSlice } from "./ProductsSlice"
import { companiesSlice } from "./CompaniesSlice";
import { reviewsSlice } from "./ReviewsSlice";
import { authSlice} from './AuthSlice';
import thunk from 'redux-thunk'

export const store = configureStore(
    {
        reducer: {
            products: productsSlice.reducer,
            companies: companiesSlice.reducer,
            reviews: reviewsSlice.reducer,
            auth: authSlice.reducer,
        },
        middleware: [thunk],
    }
);

