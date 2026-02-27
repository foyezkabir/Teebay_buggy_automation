import React from 'react';
import { Button } from 'semantic-ui-react';

import {
  StyledContainer, StyledTitle, StyledCategories, StyledPriceHolder, StyledPurchasePrice,
  StyledDescription, StyledCardFooter, StyledMainContent, StyledHeader,
} from './productCard.styles';

const ProductCard = ({ product, deleteButtonHandler, onClick }) => {
  const {
    title, description, categories, created_at, views, purchase_price, rent_price,
    rent_duration_type
  } = product;

  return(
    <StyledContainer>
      <StyledMainContent>
        <StyledHeader>
          <StyledTitle onClick={onClick}>{title}</StyledTitle>
          { deleteButtonHandler &&
            <Button icon="trash" onClick={() => deleteButtonHandler()}/>
          }
        </StyledHeader>
        <StyledCategories onClick={onClick}>Categories: { categories.length > 0 ? categories.map(c => c.name).join(", "): "N/A"}</StyledCategories>
        <StyledPriceHolder onClick={onClick}>
          <StyledPurchasePrice>Price: ${purchase_price}</StyledPurchasePrice>
          <div>Rent: ${rent_price} {rent_duration_type}</div>
        </StyledPriceHolder>
        <StyledDescription onClick={onClick}>Description: {description}</StyledDescription>
      </StyledMainContent>
      <StyledCardFooter onClick={onClick}>
        <div>
          Date posted: { created_at }
        </div>
        <div>
          { views } views
        </div>
      </StyledCardFooter>
    </StyledContainer>
  );
};

export default ProductCard;
