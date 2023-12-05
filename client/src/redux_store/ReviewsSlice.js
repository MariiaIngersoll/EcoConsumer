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
    updateReview: (state, action) => {
      const updatedReview = action.payload;
      state.reviewsForProduct = state.reviewsForProduct.map(review =>
        review.id === updatedReview.id ? updatedReview : review 
        );
    },
  },
});

export const { setReviewsForProduct, addReview, updateReview } = reviewsSlice.actions;

export default reviewsSlice.reducer;