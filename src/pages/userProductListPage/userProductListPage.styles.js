import styled from 'styled-components';

const StyledProductList = styled.div`
  flex: 1 1 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`

const StyledProductCardHolder = styled.div`
  margin-bottom: 10px;
`

const StyledButtonHolder = styled.div`
  display: flex;
  justify-content: flex-end;
  width: 100%;
  margin-bottom: 20px;
  margin-right: 10em;
`;

export { StyledProductList, StyledProductCardHolder, StyledButtonHolder };
