import { Routes, Route } from "react-router-dom";
import { ToastContainer } from 'react-toastify';
import { useSelector } from 'react-redux';
import 'react-toastify/dist/ReactToastify.css';

import { RequireAuth, NavigationBar } from 'shared/components';
import { NOT_LOGGED_IN_STATUS, LOGGED_IN_STATUS } from 'slices/currentUser';

import {
  SignInPage, RegistrationPage, UserProductListPage, AccountSettingsPage, AddProductPage,
  EditProductPage, BrowseProductsPage, ProductDetailsPage,
} from './pages';
import { StyledAppContainer } from './App.styles';

function App() {
  const { status } = useSelector((state) => state.currentUser);
  return (
    <>
      {
        status === LOGGED_IN_STATUS &&
        <NavigationBar />
      }
      <StyledAppContainer isPreLogin={status === NOT_LOGGED_IN_STATUS}>
        <Routes>
          <Route
            path="/"
            element={
              // <PreSignIn>
                <SignInPage />
              // </PreSignIn>
            }
          />
          <Route
            path="signin"
            element={
              // <PreSignIn>
                <SignInPage />
              // </PreSignIn>
            }
          />
          <Route
            path="register"
            element={
              // PreSignIn doesnt work
              // <PreSignIn>
                <RegistrationPage />
              // </PreSignIn>
            }
          />
          <Route
            path="my-products"
            element={
              <RequireAuth >
                <UserProductListPage />
              </RequireAuth>
            }
          />
          <Route
            path="add-product"
            element={
              <RequireAuth >
                <AddProductPage />
              </RequireAuth>
            }
          />
          <Route
            path="browse-products"
            element={
              <RequireAuth >
                <BrowseProductsPage />
              </RequireAuth>
            }
          />
          <Route
            path="edit-product/:productId"
            element={
              <RequireAuth >
                <EditProductPage />
              </RequireAuth>
            }
          />
          <Route
            path="product-details/:productId"
            element={
              <RequireAuth >
                <ProductDetailsPage />
              </RequireAuth>
            }
          />
          <Route
            path="account-settings"
            element={
              <RequireAuth >
                <AccountSettingsPage />
              </RequireAuth>
            }
          />
          <Route
            path="*"
            element={
              status === NOT_LOGGED_IN_STATUS ? <SignInPage /> : <UserProductListPage />
            }
          />
        </Routes>
      </StyledAppContainer>
      <ToastContainer />
    </>
  );
}

export default App;
