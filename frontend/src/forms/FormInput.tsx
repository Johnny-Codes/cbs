import React from "react";

type FormInputProps = {
  type: string;
} & React.InputHTMLAttributes<HTMLInputElement>;

const FormInput: React.FC<FormInputProps> = ({ type, ...rest }) => {
  return (
    <input type={type} {...rest} />
  );
};

export default FormInput;