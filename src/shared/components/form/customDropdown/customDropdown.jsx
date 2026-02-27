import React from 'react';
import { Form, Label, Dropdown } from 'semantic-ui-react';
import { useFormContext } from 'react-hook-form';

const CustomDropdown = ({ labelName, name, ...rest }) => {
  const { register, setValue, formState: { errors } } = useFormContext();

  return(
    <Form.Field>
      { labelName &&
        <label>{labelName}</label>
      }
        <Dropdown
          {...rest}
          {...register(name)}
          error={!!errors[name]}
          onChange={(e, { value }) => setValue(name, value, { shouldValidate: true })}
        />
      {
        errors[name] &&
        <Label pointing prompt>{errors[name].message}</Label>
      }
    </Form.Field>
  )
};

export default CustomDropdown;
