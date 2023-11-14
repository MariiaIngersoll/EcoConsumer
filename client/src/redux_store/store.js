import { configureStore } from "@reduxjs/toolkit"
import { productsSlice } from "./ProductsSlice"
import { companiesSlice } from "./CompaniesSlice";
import { reviewsSlice } from "./ReviewsSlice";

export const store = configureStore(
    {
        reducer: {
            products: productsSlice.reducer,
            companies: companiesSlice.reducer,
            reviews: reviewsSlice.reducer,
        },
    }
);

