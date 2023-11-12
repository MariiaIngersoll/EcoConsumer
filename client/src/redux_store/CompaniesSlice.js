import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    companies: [],
    singleCompany: null,
};

export const companiesSlice = createSlice({
    name: "companies",
    initialState,
    reducers: {
        setCompanies: (state, action) => {
            state.companies = action.payload;
        },
        setSingleCompany: (state, action) => {
            state.singleCompany = action.payload;
          },
    },
});

export const { setCompanies, setSingleCompany } = companiesSlice.actions;
export default companiesSlice.reducer