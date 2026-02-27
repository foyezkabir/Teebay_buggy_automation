import React from 'react';
import { useLocation, Navigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { toast } from 'react-toastify';

import { LOGGED_IN_STATUS, NOT_LOGGED_IN_STATUS } from 'slices/currentUser';

const RequireAuth = ({ children }) => {
  const location = useLocation();
  const { status } = useSelector((state) => state.currentUser);

  if (status === NOT_LOGGED_IN_STATUS) {
    // Redirect them to the /login page, but save the current location they were
    // trying to go to when they were redirected. This allows us to send them
    // along to that page after they login, which is a nicer user experience
    // than dropping them off on the home page.
    toast.error('You need to login in order to see this page!', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });

    return <Navigate to="/signin" state={{ from: location }} replace />;
  }

  return children;
}

const PreSignIn = ({ children }) => {
  const { status } = useSelector((state) => state.currentUser);

  // BUG: Uncomment to debug the PreSignIn component
  // console.log("PRE SIGN IN CALLED", children);

  if (status === LOGGED_IN_STATUS) {
    // Redirect them to the current page as you are already logged in
    toast.error('You are already logged in!', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });

    return null;
    // return <Navigate to={location.pathname} replace />;
  }

  return children;
}

export { RequireAuth, PreSignIn };
