import React from 'react';
import { Header } from 'semantic-ui-react';

import { SignInForm } from './components';
import { StyledSignInPageContainer } from './signInPage.styles'

const SignInPage = () => (
  <StyledSignInPageContainer>
    <Header as='h1'>SIGN IN</Header>
    <SignInForm />
  </StyledSignInPageContainer>
);

export default SignInPage;
