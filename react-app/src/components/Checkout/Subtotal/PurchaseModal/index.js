import React from 'react'
import {Modal} from '../../../../context/Modal'
import './PurchaseModal.css'

function PurchaseModal({showPurchaseModal, setShowPurchaseModal}) {
  return (
    <Modal className="purchasemodal">
        <div className='purchasemodal'>

    <div className='complete'>Purchase Complete!</div>
    <div className='completedescription'>Products can be viewed in your order history</div>
        </div>
  </Modal>
  )
}

export default PurchaseModal
