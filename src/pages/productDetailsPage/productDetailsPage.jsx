import React, { useEffect, useState } from 'react';
import { Header, Label, Button } from 'semantic-ui-react';
import { useParams, useNavigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { toast } from 'react-toastify';
import isBefore from 'date-fns/isBefore';
import isAfter from 'date-fns/isAfter';
import format from 'date-fns/format';
import { useForm } from "react-hook-form";

import { addViewToProduct, purchaseProduct, rentProduct } from 'slices/allProducts';
import { CustomModal } from 'shared/components';
import { useModal } from 'hooks';

import { RentForm } from './components';

import {
  StyledTitle, StyledCategories, StyledDescription, StyledStatus, StyledPrice, StyledTitleHolder,
  StyledHeaderHolder, StyledDatePosted, StyledButtonsHolder, StyledProductDetailsPageContainer,
  StyledRentHistory,
} from './productDetailsPage.styles';

const ProductDetailsPage = (props) => {
  const params = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const methods = useForm();
  const allProducts = useSelector((state) => state.allProducts);
  const userProducts = useSelector((state) => state.userProducts);
  const [ currentProduct, setCurrentProduct ] = useState(null);
  const [purchaseModalOpen, setPurchaseModalOpen] = useModal();
  const [rentModalOpen, setRentModalOpen] = useModal();

  useEffect(() => {
    if (isNaN(parseInt(params.productId))) {
      toast.error('Invalid product id!', {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      navigate('/my-products');
    } else {
      const product = allProducts.find(p => p.id === parseInt(params.productId));
      if (!product) {
        toast.warn('Product does not exist!', {
          position: "top-right",
          autoClose: 3000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
        });
        navigate('/my-products');
      } else {
        if (product % 2 !== 0) {
          dispatch(addViewToProduct(product.id));
        }
        setCurrentProduct({ ...product, views: product.views + 1 });
      }
    }
  }, []);

  const getDateObject = (dateString) => {
    const dateElements = dateString.split('-');
    return new Date(parseInt(dateElements[0]), parseInt(dateElements[1]), parseInt(dateElements[2]));
  }

  const isCurrentlyRented = () => {
    const currentYear = new Date().getFullYear();
    const currentMonth = new Date().getMonth() + 1;
    const currentDate = new Date().getDate();

    return !!currentProduct.rent_history.find(dateRange =>
      isBefore(new Date(currentYear, currentMonth, currentDate), getDateObject(dateRange.end_date)) &&
      isAfter(new Date(currentYear, currentMonth, currentDate), getDateObject(dateRange.start_date))
    );
  }

  const getStatusAndColor = () => {
    if (currentProduct.is_purchased) {
      return {
        color: 'red',
        statusText: 'SOLD',
      };
    } else if (isCurrentlyRented()) {
      return {
        color: 'orange',
        statusText: 'CURRENTLY RENTED'
      }
    }

    return {
      color: 'green',
      statusText: 'Available'
    }
  }

  const isUserProduct = () => {
    return !!userProducts.find(p => p.id === currentProduct.id);
  }

  const purchaseModalButtonHandler = () => {
    dispatch(purchaseProduct(currentProduct.id));
    setCurrentProduct({ ...currentProduct, is_purchased: true });
    setPurchaseModalOpen(false);
  }

  const rentModalButtonHandler = (data) => {
    dispatch(rentProduct({ id: currentProduct.id, ...data }));
    setCurrentProduct({ ...currentProduct, rent_history: [...currentProduct.rent_history, data]});
    setRentModalOpen(false);
  }

  if (!currentProduct) {
    return(<></>);
  }

  return(
    <StyledProductDetailsPageContainer>
      <CustomModal
        mainSection="Are you sure you want to buy this product?"
        primaryButtonHandler={purchaseModalButtonHandler}
        primaryButtonText="Yes!"
        itemModalOpen={purchaseModalOpen}
        setItemModalOpen={setPurchaseModalOpen}
      />
      <CustomModal
        mainSection={<RentForm formMethods={methods} />}
        primaryButtonHandler={methods.handleSubmit((data) => rentModalButtonHandler(data))}
        primaryButtonText="Book rent"
        itemModalOpen={rentModalOpen}
        setItemModalOpen={setRentModalOpen}
      />
      <StyledHeaderHolder>
        <Header as='h1'>PRODUCT DETAILS</Header>
      </StyledHeaderHolder>
      <StyledTitleHolder>
        <StyledTitle>{currentProduct.title}</StyledTitle>
        <div>Views: {currentProduct.views}</div>
      </StyledTitleHolder>
      <StyledCategories>Categories: { currentProduct.categories.length > 0 ? currentProduct.categories.map(c => c.name).join(", "): "N/A"}</StyledCategories>
      <StyledStatus>Status: <Label color={getStatusAndColor().color}>{getStatusAndColor().statusText}</Label> { isUserProduct() && <Label color='blue'>You own the product</Label>}</StyledStatus>
      <StyledPrice>Purchase Price: ${currentProduct.purchase_price} | Rent Price: ${currentProduct.rent_price} {currentProduct.rent_duration_type}</StyledPrice>
      <StyledDatePosted></StyledDatePosted>
      <StyledDescription>{currentProduct.description}</StyledDescription>
      <StyledRentHistory>Rent history: {currentProduct.rent_history.map(dateRange => `(${format(getDateObject(dateRange.start_date), "MMM do yyyy")} - ${format(getDateObject(dateRange.end_date), "MMM do yyyy")})`).join(", ")}</StyledRentHistory>
      { !currentProduct.is_purchased && !isUserProduct() &&
        <StyledButtonsHolder>
          <Button color='teal' onClick={() => setRentModalOpen(true)}>Rent</Button>
          <Button color='blue' onClick={() => setPurchaseModalOpen(true)}>Buy</Button>
        </StyledButtonsHolder>
      }
    </StyledProductDetailsPageContainer>
  );
};

export default ProductDetailsPage;
