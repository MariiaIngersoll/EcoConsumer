import { createSlice } from '@reduxjs/toolkit';

export const sessionSlice = createSlice({
    name: 'session',
    initialState: {
        user: null,
    },
    reducers: {
        setUser: (state, action) => {
            state.user = action.payload;
        },

    },
});

export const {setUser} = sessionSlice.actions;
export default sessionSlice.reducer;