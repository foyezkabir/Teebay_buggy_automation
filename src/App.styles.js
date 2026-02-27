import styled, { css } from 'styled-components';

const StyledAppContainer = styled.div`
  display: flex;

  ${
    props => props.isPreLogin && css`
    height: 100%;
  `}
`

export { StyledAppContainer };
