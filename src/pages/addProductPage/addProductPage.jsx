import React from 'react';
import { Header } from 'semantic-ui-react';

import { UpsertProductForm } from 'shared/components';

import { StyledAddProductPageContainer } from './addProductPage.styles'

const AddProductPage = () => {
  return(
    <StyledAddProductPageContainer>
      <Header as='h1'>ADD PRODUCT</Header>
      <UpsertProductForm />
    </StyledAddProductPageContainer>
  );
};

export default AddProductPage;
