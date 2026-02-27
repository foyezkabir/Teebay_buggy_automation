import styled from 'styled-components';

const StyledTitle = styled.div`
  font-weight: bold;
  font-size: 30px;
  padding-bottom: 0.5em;
`;

const StyledCategories = styled.div`
  padding-bottom: 0.5em;
`;

const StyledDescription = styled.div`
  padding-bottom: 0.5em;
`

const StyledStatus = styled.div`
  padding-bottom: 0.5em;
`

const StyledPrice = styled.div`
  padding-bottom: 0.5em;
`

const StyledTitleHolder = styled.div`
  display: flex;
  justify-content: space-between;
`

const StyledHeaderHolder = styled.div`
  display: flex;
  justify-content: center;
  margin-bottom: 3em;
`

const StyledDatePosted = styled.div`
  padding-bottom: 0.5em;
`

const StyledButtonsHolder = styled.div`
  display: flex;
  margin-top: 8em;
  justify-content: flex-end;
`

const StyledProductDetailsPageContainer = styled.div`
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  padding: 5em 15em;
`

const StyledRentHistory = styled.div`
  padding-bottom: 0.5em;
`;

export {
  StyledTitle, StyledCategories, StyledDescription, StyledStatus, StyledPrice, StyledTitleHolder,
  StyledHeaderHolder, StyledDatePosted, StyledButtonsHolder, StyledProductDetailsPageContainer,
  StyledRentHistory,
};
