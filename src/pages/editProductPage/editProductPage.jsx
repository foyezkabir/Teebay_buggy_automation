import React from 'react';
import { Header } from 'semantic-ui-react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { toast } from 'react-toastify';

import { UpsertProductForm } from 'shared/components';

import { StyledPageContainer } from 'shared/styles';

const EditProductPage = (props) => {
  const params = useParams();
  const userProducts = useSelector((state) => state.userProducts);

  if (isNaN(parseInt(params.productId))) {
    toast.error('Internal server error occurred!', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
    console.error("SERVER ERROR: Invalid product id sent!", params.productId);
    return(
      <StyledPageContainer>
        <Header as='h1'>EDIT PRODUCT</Header>
      </StyledPageContainer>
    );
  }

  const product = userProducts.find(p => p.id === parseInt(params.productId));

  return(
    <StyledPageContainer>
      <Header as='h1'>EDIT PRODUCT</Header>
      { product &&
        <UpsertProductForm isEdit product={product} />
      }
    </StyledPageContainer>
  );
};

export default EditProductPage;
