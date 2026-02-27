import React from 'react';
import { Button, Form } from 'semantic-ui-react';
import * as yup from 'yup';
import { useForm, FormProvider } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import { Link } from "react-router-dom";
import { toast } from 'react-toastify';

import { CustomInput } from 'shared/components';
import {
  StyledRegistrationFormBorder, StyledRegistrationFormContainer,
  StyledTextHolder, StyledText, StyledButtonHolder,
} from './registrationForm.styles';

const registrationSchema = yup.object().shape({
  lastName: yup.string().required('Last Name is required'),
  address: yup.string().required('Address is required'),
  email: yup.string().email('Please enter a valid email address').required('Email is required'),
  phoneNumber: yup.string().required('Phone number is required'),
  password: yup.string().required('Password is required'),
}).required();

const RegistrationForm = () => {
  const methods = useForm({
    resolver: yupResolver(registrationSchema),
  });

  const onSubmitHandler = (data) => {
    toast.error('Internal error occurred. Please check the server!', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
    console.error("SERVER ERROR: Internal server occurred!");
  }

  return(
    <FormProvider {...methods} >
      <StyledRegistrationFormBorder>
        <StyledRegistrationFormContainer>
          <Form onSubmit={methods.handleSubmit(onSubmitHandler)}>
            <Form.Group widths="equal">
              <CustomInput labelName="First Name" name="firstName" />
              <CustomInput labelName="Last Name" name="lastName" />
            </Form.Group>
            <CustomInput labelName="Address" name="address" />
            <Form.Group widths="equal">
              <CustomInput labelName="Email" name="email" />
              <CustomInput labelName="Phone Number" name="phoneNumber" />
            </Form.Group>
            <CustomInput labelName="Password" name="password" type="password" />
            <CustomInput labelName="Confirm Password" name="confirmPassword" type="password" />
            <StyledTextHolder>
              <StyledText>Already have an account?</StyledText><Link to="/signin">Sign In</Link>
            </StyledTextHolder>
            <StyledButtonHolder>
              <Button color='blue' type='submit'>Register</Button>
            </StyledButtonHolder>
          </Form>
        </StyledRegistrationFormContainer>
      </StyledRegistrationFormBorder>
    </FormProvider>
  );
}

export default RegistrationForm;
