import React, { useState } from "react";
import { Modal } from "../../../../context/Modal";
import "./PurchaseModal.css";

function PurchaseModal({
  showPurchaseModal,
  setShowPurchaseModal,
  total,
}) {
  const [submitTotal, setSubmitTotal] = useState(total)
  return (
    <Modal className="purchasemodal">
      <div className="purchasemodal">
        <div className="complete">Purchase Complete!</div>
        <div className="complete"> You spent: ${Number.parseFloat(submitTotal).toFixed(2)}</div>
        <div className="completedescription">
          Products can be viewed in your order history
        </div>
      </div>
    </Modal>
  );
}

export default PurchaseModal;
