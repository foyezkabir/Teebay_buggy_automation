import styled from 'styled-components';

const StyledTextArea = styled.textarea`
  &&&& {
    border-color: ${props => props.error ? "red" : "#22242626"};
  }
`;

export { StyledTextArea };
