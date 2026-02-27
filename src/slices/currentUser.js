import { createSlice } from '@reduxjs/toolkit'

import user from 'testData/user';

export const NOT_LOGGED_IN_STATUS = 'not_logged_in';
export const LOGGED_IN_STATUS = 'logged_in';

const initialState = {
  status: NOT_LOGGED_IN_STATUS,
}

const currentUserSlice = createSlice({
  name: 'currentUser',
  initialState,
  reducers: {
    logIn(state, action) {
      state.status = LOGGED_IN_STATUS;
    },
    logOut(state, action) {
      state.status = NOT_LOGGED_IN_STATUS;
    },
    loadUser(state) {
      state = { ...state, ...user };
      return state;
    },
    editUser(state, action) {
      state = { ...state, ...action.payload };
      return state;
    }
  }
})

export const { logIn, logOut, loadUser, editUser } = currentUserSlice.actions

export default currentUserSlice.reducer
