import { createSlice } from '@reduxjs/toolkit';

export const reviewsSlice = createSlice({
  name: 'reviews',
  initialState: {
    reviewsForProduct: [],
  },
  reducers: {
    setReviewsForProduct: (state, action) => {
      state.reviewsForProduct = action.payload;
    },
    addReview: (state, action) => {
      state.reviewsForProduct.push(action.payload);
    },
  },
});

export const { setReviewsForProduct, addReview } = reviewsSlice.actions;

export default reviewsSlice.reducer;