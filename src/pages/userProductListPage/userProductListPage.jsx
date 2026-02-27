import React, { useRef } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { toast } from 'react-toastify';
import { Button } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';

import { ProductCard } from 'shared/components';
import { randomIdGenerator } from 'utils';
import { deleteProduct } from 'slices';
import { useModal } from 'hooks';
import { CustomModal } from 'shared/components';

import { StyledProductList, StyledProductCardHolder, StyledButtonHolder } from './userProductListPage.styles';

const UserProductListPage = () => {
  const userProducts = useSelector(state => state.userProducts);
  const idToDelete = useRef(null);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [itemModalOpen, setItemModalOpen] = useModal();

  const modalPrimaryButtonHandler = () => {
    dispatch(deleteProduct(idToDelete.current));
    setItemModalOpen(false);
  }

  const deleteButtonHandler = (id) => {
    if (userProducts.length === 1) {
      toast.error('Internal server error occurred. Please check the server!', {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      console.error("SERVER ERROR: Undefined method [] for nil:NilClass");
    } else {
      idToDelete.current = id;
      setItemModalOpen(true);
    }
  }

  if (userProducts.length === 0) {
    return(
      <>You do not have any products!</>
    );
  }

  return(
    <>
      <CustomModal
        mainSection="Are you sure you want to delete this product?"
        primaryButtonHandler={modalPrimaryButtonHandler}
        primaryButtonText="Yes, delete"
        itemModalOpen={itemModalOpen}
        setItemModalOpen={setItemModalOpen}
      />
      <StyledProductList>
        <StyledButtonHolder>
          <Button color='blue' onClick={() => navigate('/add-product') }>
            Add Product
          </Button>
        </StyledButtonHolder>
        {
          userProducts.map(product =>
            <div key={randomIdGenerator()}>
              <StyledProductCardHolder key={randomIdGenerator()}>
                <ProductCard
                  product={product}
                  deleteButtonHandler={() => deleteButtonHandler(product.id)}
                  onClick={() => navigate(`/edit-product/${product.id}`)}
                />
              </StyledProductCardHolder>
              <StyledProductCardHolder key={randomIdGenerator()}>
                <ProductCard
                  product={product}
                  deleteButtonHandler={() => deleteButtonHandler(product.id)}
                  onClick={() => navigate(`/edit-product/${product.id}`)}
                />
              </StyledProductCardHolder>
            </div>
          )
        }
      </StyledProductList>
    </>
  )
};

export default UserProductListPage;
