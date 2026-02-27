import React from 'react';
import { Form, Label } from 'semantic-ui-react';
import { useFormContext } from 'react-hook-form';

import { StyledInput } from './customInput.styles';

const CustomInput = ({ labelName, name, ...rest }) => {
  const { register, formState: { errors } } = useFormContext();

  return(
    <Form.Field>
      { labelName &&
        <label>{labelName}</label>
      }
        <StyledInput {...rest} {...register(name)} error={errors[name]} />
      {
        errors[name] &&
        <Label pointing prompt>{errors[name].message}</Label>
      }
    </Form.Field>
  )
};

export default CustomInput;
