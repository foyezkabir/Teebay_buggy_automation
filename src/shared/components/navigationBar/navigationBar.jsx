import React, { useState } from 'react';
import { Menu } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import CustomModal from 'shared/components/customModal/customModal';
import { useModal } from 'hooks';
import { logOut } from 'slices/currentUser';

const NavigationBar = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [ activeItem, setActiveItem ] = useState('my-products');
  const [itemModalOpen, setItemModalOpen] = useModal();

  const handleItemClick = (e, { name }) => {
    setActiveItem(name);
    navigate(`/${name}`);
  }

  const handleLogout = () => {
    dispatch(logOut());
    setItemModalOpen(false);
    navigate('/signin');
  }

  return(
    <>
      <CustomModal
        mainSection="Are you sure you want to log out?"
        primaryButtonHandler={handleLogout}
        primaryButtonText="Yes I am sure!"
        itemModalOpen={itemModalOpen}
        setItemModalOpen={setItemModalOpen}
      />
      <Menu>
        <Menu.Item
          name='my-products'
          active={activeItem === 'my-products'}
          onClick={handleItemClick}
        />
        <Menu.Item
          name='browse-products'
          active={activeItem === 'browse-products'}
          onClick={handleItemClick}
        />
        <Menu.Item
          name='categorize-products'
          active={activeItem === 'categorize-products'}
          onClick={() => itemModalOpen()}
        >
          Bought/Sold/Borrowed/Lent List
        </Menu.Item>
        <Menu.Item
          name='account-settings'
          active={activeItem === 'account-settings'}
          onClick={handleItemClick}
        />
        <Menu.Menu position='right'>
          <Menu.Item
            name='logout'
            active={activeItem === 'logout'}
            onClick={() => setItemModalOpen(true)}
          />
        </Menu.Menu>
      </Menu>
    </>
  );
};

export default NavigationBar;
