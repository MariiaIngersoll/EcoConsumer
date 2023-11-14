import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    products: [],
    singleProduct: {},
};

export const productsSlice = createSlice({
    name: "products",
    initialState,
    reducers: {
        setProducts: (state, action) => {
            state.products = action.payload;
        },
        setSingleProduct: (state, action) => {
            state.singleProduct = action.payload
        },
    },
});

export const { setProducts, setSingleProduct } = productsSlice.actions;
export default productsSlice.reducer