import React from 'react';
import { Header } from 'semantic-ui-react';

import { RegistrationForm } from './components/registrationForm';
import { StyledRegistrationPageContainer } from './registrationPage.styles'

const RegistrationPage = () => (
  <StyledRegistrationPageContainer>
    <Header as='h1'>REGISTRATION</Header>
    <RegistrationForm />
  </StyledRegistrationPageContainer>
);

export default RegistrationPage;
