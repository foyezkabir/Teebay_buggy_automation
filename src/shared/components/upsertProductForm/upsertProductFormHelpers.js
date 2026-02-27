import * as yup from 'yup';

import categories from 'testData/categories';

function convertDataToDropdownOptions() {
  return categories.map((category, index) => ({
    key: index,
    text: category.name,
    value: category.name,
  }));
};

function convertCategoriesForSubmission(categoryList) {
  return categoryList.map(cl => categories.find(c => c.name === cl));
}

function getSchema(isEdit) {
  const baseSchemaObject = {
    title: yup.string().required('Last Name is required'),
    categories: yup.array().of(yup.string()).required("At least one category must be selected"),
    description: yup.string().required('Description cannot be empty'),
    rent_duration_type: yup.string().required('Need to select an option'),
  }

  const addSchemaObject = {
    purchase_price: yup.number().typeError('Purchase price must be a number').required('Purchase price is required'),
    rent_price: yup.number().typeError('Rent price must be a number').required('Rent price is required'),
  }

  const editSchemaObject = {
    purchase_price: yup.string().required('Purchase price is required'),
    rent_price: yup.string().required('Rent price is required'),
  }

  const updatedSchemaObject = { ...baseSchemaObject, ...(isEdit ? editSchemaObject : addSchemaObject) };

  return yup.object(updatedSchemaObject).shape().required();
}

export { convertDataToDropdownOptions, convertCategoriesForSubmission, getSchema };
