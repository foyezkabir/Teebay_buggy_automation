import React from 'react';
import { Button, Modal } from 'semantic-ui-react';

const CustomModal = ({
  header, mainSection, primaryButtonHandler, primaryButtonText,
  itemModalOpen, setItemModalOpen
}) => {
  return(
    <Modal
        onClose={() => setItemModalOpen(false)}
        onOpen={() => setItemModalOpen(true)}
        open={itemModalOpen}
      >
      {
        header &&
        <Modal.Header>{header}</Modal.Header>
      }
      <Modal.Content>
        <Modal.Description>
          { mainSection }
        </Modal.Description>
      </Modal.Content>
      <Modal.Actions>
        <Button color='red' onClick={() => setItemModalOpen(false)}>
          Cancel
        </Button>
        <Button
          color='blue'
          onClick={() => primaryButtonHandler()}
        >
          {primaryButtonText}
        </Button>
      </Modal.Actions>
    </Modal>
  );
};

export default CustomModal;
