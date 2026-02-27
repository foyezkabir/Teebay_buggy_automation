import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { Button, Loader } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

import additionalProducts from 'testData/additionalProducts';
import { ProductCard } from 'shared/components';
import { randomIdGenerator } from 'utils';

import { FilterForm } from './components';
import {
  StyledLeftSection, StyledRightSection, StyledBrowsePageHolder, StyledProductCardHolder,
  StyledButtonHolder, StyledLoaderHolder, StyledNoProductText,
} from './browseProductsPage.styles';

const BrowseProductsPage = () => {
  const navigate = useNavigate();
  const userProducts = useSelector((state) => state.userProducts);
  const allProducts = useSelector((state) => state.allProducts);
  const [showLoader, setShowLoader] = useState(false);
  const [filteredProducts, setFilteredProducts] = useState(allProducts);

  const loadButtonOnClickHandler = () => {
    setShowLoader(true);
    setTimeout(() => {
      toast.error('Request timed out!', {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      console.error("SERVER ERROR: Request timeout!");
    }, 5000)
  }

  const filterProducts = (data) => {
    // Bug fix!
    // let updatedFilteredProducts = [...additionalProducts, ...userProducts];
    let updatedFilteredProducts = filteredProducts;

    if (data.category) {
      updatedFilteredProducts = updatedFilteredProducts.filter(fp => fp.categories.map(p => p.name).includes(data.category));
    }

    if (data.is_buy_filter_turned_on) {
      updatedFilteredProducts = updatedFilteredProducts.filter(fp => {
        if (data.min_buy_range && data.max_buy_range) {
          return fp.purchase_price > parseInt(data.min_buy_range) && fp.purchase_price < parseInt(data.max_buy_range);
        } else if (data.min_buy_range) {
          return fp.purchase_price > parseInt(data.min_buy_range);
        } else {
          return fp.purchase_price < parseInt(data.max_buy_range)
        }
      });
    }

    if (data.is_rent_filter_turned_on) {
      updatedFilteredProducts = updatedFilteredProducts.filter(fp => {
        if (data.min_rent_range && data.max_rent_range) {
          return fp.rent_price >= parseInt(data.min_rent_range) && fp.rent_price <= parseInt(data.max_rent_range);
        } else if (data.min_rent_range) {
          return fp.rent_price >= parseInt(data.min_rent_range);
        } else {
          return fp.rent_price <= parseInt(data.max_rent_range)
        }
      });

      if (data.rent_duration_type) {
        updatedFilteredProducts = updatedFilteredProducts.filter(fp => fp.rent_duration_type === data.rent_duration_type);
      }
    }

    setFilteredProducts(updatedFilteredProducts);
  }

  const resetFilteredProducts = () => {
    setFilteredProducts([...additionalProducts, ...userProducts]);
  }

  return(
    <StyledBrowsePageHolder>
      <StyledLeftSection>
        <FilterForm onSubmitHandler={filterProducts} resetFilteredProducts={resetFilteredProducts} />
      </StyledLeftSection>
      <StyledRightSection>
        { filteredProducts.length === 0 ?
          <StyledNoProductText>
            No products to display
          </StyledNoProductText> :
          filteredProducts.map(product =>
            <StyledProductCardHolder key={randomIdGenerator()}>
              <ProductCard
                product={product}
                onClick={() => navigate(`/product-details/${product.id}`)}
              />
            </StyledProductCardHolder>
          )
        }
        {
          showLoader &&
          <StyledLoaderHolder>
            <Loader size='large' inline active>
              Loading
            </Loader>
          </StyledLoaderHolder>
        }
        { filteredProducts.length > 0 &&
          <StyledButtonHolder>
            <Button color='blue' onClick={loadButtonOnClickHandler}>Load More</Button>
          </StyledButtonHolder>
        }
      </StyledRightSection>
    </StyledBrowsePageHolder>
  );
};

export default BrowseProductsPage;
