import styled from 'styled-components'

const StyledRegistrationFormBorder = styled.div`
  border: 1px solid black;
  min-width: 35%;
  min-height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
`

const StyledRegistrationFormContainer = styled.div`
  min-width: 80%;
  padding: 3rem;
`

const StyledTextHolder = styled.div`
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: center;
`

const StyledText = styled.div`
  margin-right: 5px;
`

const StyledButtonHolder = styled.div`
  margin-top: 30px;
  display: flex;
  justify-content: center;
`

export {
  StyledRegistrationFormBorder, StyledRegistrationFormContainer, StyledTextHolder, StyledText,
  StyledButtonHolder,
};
