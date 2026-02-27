import { combineReducers } from 'redux';

import currentUserReducer from '../slices/currentUser';
import userProductsReducer from '../slices/userProducts';
import allProductsReducer from '../slices/allProducts';

const rootReducer = combineReducers({
  currentUser: currentUserReducer,
  userProducts: userProductsReducer,
  allProducts: allProductsReducer,
});

export default rootReducer
