import styled from 'styled-components';

const StyledInput = styled.input`
  &&&& {
    border-color: ${props => props.error ? "red" : "#22242626"};
  }
`;

export { StyledInput };
