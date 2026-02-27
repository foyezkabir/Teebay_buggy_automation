import { createSlice } from '@reduxjs/toolkit'

const initialState = [];

const allProductsSlice = createSlice({
  name: 'allProducts',
  initialState,
  reducers: {
    rentProduct(state, action) {
      const productIndexToRent = state.findIndex(p => p.id === action.payload.id);
      state[productIndexToRent] = {
        ...state[productIndexToRent],
        rent_history: [ ...state[productIndexToRent].rent_history, { start_date: action.payload.start_date, end_date: action.payload.end_date }],
      };

      return state;
    },
    purchaseProduct(state, action) {
      const productIndexToBuy = state.findIndex(p => p.id === action.payload);
      state[productIndexToBuy] = { ...state[productIndexToBuy], is_purchased: true };

      return state;
    },
    addViewToProduct(state, action) {
      const productIndexToBuy = state.findIndex(p => p.id === action.payload);
      state[productIndexToBuy].views = state[productIndexToBuy].views + 1;

      return state;
    },
    loadAllProducts(state, action) {
      state = action.payload;

      return state;
    },
  }
})

export const { rentProduct, purchaseProduct, loadAllProducts, addViewToProduct } = allProductsSlice.actions

export default allProductsSlice.reducer
