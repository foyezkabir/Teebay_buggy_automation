import React from 'react';
import { Button, Form } from 'semantic-ui-react';
import * as yup from 'yup';
import { useForm, FormProvider } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import { toast } from 'react-toastify';
import { useSelector, useDispatch } from 'react-redux';

import { CustomInput } from 'shared/components';
import { editUser } from 'slices';

import {
  StyledAccountSettingsFormBorder, StyledAccountSettingsFormContainer, StyledButtonHolder,
} from './accountSettingsForm.styles';

const accountSettingsSchema = yup.object().shape({
  first_name: yup.string().required('First Name is required'),
  last_name: yup.string().required('Last Name is required'),
  address: yup.string().required('Address is required'),
  email: yup.string().email('Please enter a valid email address').required('Email is required'),
  phone_number: yup.number('Only number is accepted').required('Phone number is required'),
}).required();

const AccountSettingsForm = () => {
  const dispatch = useDispatch();
  const { status, ...rest } = useSelector((state) => state.currentUser);
  const methods = useForm({
    resolver: yupResolver(accountSettingsSchema),
    defaultValues: rest,
  });

  const onSubmitHandler = (data) => {
    dispatch(editUser(data));
    toast.success('User updated!', {
      position: "top-right",
      autoClose: 3000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  }

  return(
    <FormProvider {...methods} >
      <StyledAccountSettingsFormBorder>
        <StyledAccountSettingsFormContainer>
          <Form onSubmit={methods.handleSubmit(onSubmitHandler)}>
            <Form.Group widths="equal">
              <CustomInput labelName="First Name" name="first_name" />
              <CustomInput labelName="Last Name" name="last_name" />
            </Form.Group>
            <CustomInput labelName="Address" name="address" />
            <Form.Group widths="equal">
              <CustomInput labelName="Email" name="email" />
              <CustomInput labelName="Phone Number" name="phone_number" />
            </Form.Group>
            <StyledButtonHolder>
              <Button color='blue' type='submit'>Update</Button>
            </StyledButtonHolder>
          </Form>
        </StyledAccountSettingsFormContainer>
      </StyledAccountSettingsFormBorder>
    </FormProvider>
  );
}

export default AccountSettingsForm;
