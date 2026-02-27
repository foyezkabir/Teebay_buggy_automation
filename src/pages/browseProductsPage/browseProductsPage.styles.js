import styled from 'styled-components';

const StyledLeftSection = styled.div`
  width: 30%;
  padding: 2em;
`;

const StyledRightSection = styled.div`
  width: 70%;
  padding: 2em;
`;

const StyledBrowsePageHolder = styled.div`
  display: flex;
  width: 100%;
`

const StyledProductCardHolder = styled.div`
  margin-bottom: 10px;
`

const StyledButtonHolder = styled.div`
  display: flex;
  justify-content: center;
`

const StyledLoaderHolder = styled(StyledButtonHolder)`
  margin: 3em;
`

const StyledNoProductText = styled(StyledButtonHolder)`
  font-size: 3em;
`

export {
  StyledLeftSection, StyledRightSection, StyledBrowsePageHolder, StyledProductCardHolder,
  StyledButtonHolder, StyledLoaderHolder, StyledNoProductText,
};
