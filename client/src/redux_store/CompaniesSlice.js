import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    companies: [],
};

export const companiesSlice = createSlice({
    name: "companies",
    initialState,
    reducers: {
        setCompanies: (state, action) => {
            state.companies = action.payload;
        },
    },
});

export const { setCompanies } = companiesSlice.actions;
export default companiesSlice.reducer