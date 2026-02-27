const CATEGORY_OPTIONS = [
  {
    key: 1,
    text: 'Sporting Goods',
    value: 'Sporting Goods',
  },
  {
    key: 2,
    text: 'Outdoor',
    value: 'Outdoor',
  },
  {
    key: 3,
    text: 'Electronics',
    value: 'Electronics',
  },
  {
    key: 4,
    text: 'Furniture',
    value: 'Furniture',
  },
  {
    key: 5,
    text: 'Home Appliances',
    value: 'Home Appliances',
  },
  {
    key: 6,
    text: 'Toys',
    value: 'Toys',
  },
]

const INITIAL_FILTER_FORM_VALUES = {
  title: '',
  category: '',
  is_buy_filter_turned_on: false,
  is_rent_filter_turned_on: false,
  min_buy_range: null,
  max_buy_range: null,
  min_rent_range: null,
  max_rent_range: null,
  rent_duration_type: '',
}

export { CATEGORY_OPTIONS, INITIAL_FILTER_FORM_VALUES };
