import styled from 'styled-components';
import { Container } from 'semantic-ui-react';

const StyledContainer = styled(Container)`
  border: 1px solid black;
  padding: 2em;
  border-radius: 5px;
  max-height: 250px;
  flex-direction: column;
  cursor: pointer;

  && {
    display: flex;
  }
`;

const StyledTitle = styled.div`
  font-weight: bold;
  font-size: 30px;
  padding-bottom: 0.5em;
`;

const StyledCategories = styled.div`
  padding-bottom: 0.5em;
`;

const StyledPriceHolder = styled.div`
  display: flex;
  padding-bottom: 0.5em;
`

const StyledPurchasePrice = styled.div`
  margin-right: 5px;
`

const StyledDescription = styled.div`
  padding-bottom: 0.5em;
`

const StyledCardFooter = styled.div`
  display: flex;
  justify-content: space-between;
  flex-grow: 1;
  align-items: flex-end;
`

const StyledMainContent = styled.div`
  display: flex;
  flex-grow: 2;
  flex-direction: column;
`

const StyledHeader = styled.div`
  display: flex;
  justify-content: space-between;
  flex-grow: 1;
`

export {
  StyledContainer, StyledTitle, StyledCategories, StyledPriceHolder, StyledPurchasePrice,
  StyledDescription, StyledCardFooter, StyledMainContent, StyledHeader
};
