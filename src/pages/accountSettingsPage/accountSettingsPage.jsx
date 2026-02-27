import React from 'react';
import { Header } from 'semantic-ui-react';

import { AccountSettingsForm } from './components';
import { StyledAccountSettingsPageContainer } from './accountSettingsPage.styles'

const AccountSettingsPage = () => (
  <StyledAccountSettingsPageContainer>
    <Header as='h1'>ACCOUNT SETTINGS</Header>
    <AccountSettingsForm />
  </StyledAccountSettingsPageContainer>
);

export default AccountSettingsPage;
