import { createSlice } from '@reduxjs/toolkit'

import userProducts from 'testData/userProducts';

const initialState = [];

const userProductsSlice = createSlice({
  name: 'userProducts',
  initialState,
  reducers: {
    deleteProduct(state, action) {
      state = state.filter(p => p.id !== action.payload);
      return state;
    },
    editProduct(state, action) {
      const productIndexToEdit = state.findIndex(p => p.id === action.payload.id);
      state[productIndexToEdit] = action.payload;
      return state;
    },
    addProduct(state, action) {
      state.push(action.payload);
      return state;
    },
    loadProducts(state) {
      state = userProducts;
      return state;
    },
  }
})

export const { addProduct, editProduct, deleteProduct, loadProducts } = userProductsSlice.actions

export default userProductsSlice.reducer
