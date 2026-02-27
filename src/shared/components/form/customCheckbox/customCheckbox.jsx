import React from 'react';
import { Form, Checkbox } from 'semantic-ui-react';
import { useFormContext } from 'react-hook-form';

const CustomCheckbox = ({ labelName, name, ...rest }) => {
  const { register } = useFormContext();

  return(
    <Form.Field>
      <Checkbox
        {...rest}
        {...register(name)}
      />
    </Form.Field>
  )
};

export default CustomCheckbox;
