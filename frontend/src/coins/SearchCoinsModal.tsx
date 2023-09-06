import React, { useState } from "react";
import AddCoinForm from "./AddCoinForm";

const SearchCoinsModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="modal-overlay" onClick={onClose}></div>
      <div className="modal-container bg-white w-3/4 mx-auto rounded shadow-lg z-50 overflow-y-auto">
        <div className="modal-content py-4 text-left px-6">
          <h1 className="text-2xl font-semibold">Add Coin</h1>
          <AddCoinForm />
          <p className="text-gray-700 my-4">Modal content goes here.</p>
          <button
            onClick={onClose}
            className="modal-close bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default SearchCoinsModal;
