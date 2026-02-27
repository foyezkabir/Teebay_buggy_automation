import React from "react";
import { Form } from 'semantic-ui-react';
import { FormProvider } from "react-hook-form";

import { CustomInput } from 'shared/components';

const RentForm = ({ onSubmitHandler, formMethods }) => {
  return (
    <FormProvider {...formMethods}>
      <Form>
        <Form.Group widths="equal">
          <CustomInput labelName="Start date" placeholder="yyyy-mm-dd" name="start_date" />
          <CustomInput labelName="Last Name" placeholder="yyyy-mm-dd" name="end_date" />
        </Form.Group>
      </Form>
    </FormProvider>
  );
}

export default RentForm;
