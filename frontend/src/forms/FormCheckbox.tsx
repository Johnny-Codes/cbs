import React from "react";

const FormCheckbox = ({ id, labelText,...rest }) => {
  return (
    <div>
      <input
        type="checkbox"
        id={id}
        {...rest}
      />
      <label htmlFor={id}>{labelText}</label>
    </div>
  );
};

export default FormCheckbox;
