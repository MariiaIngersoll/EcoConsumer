import { configureStore } from "@reduxjs/toolkit"
import { productsSlice } from "./ProductsSlice"
import { companiesSlice } from "./CompaniesSlice";
export const store = configureStore(
    {
        reducer: {
            products: productsSlice.reducer,
            companies: companiesSlice.reducer,
        },
    }
);

