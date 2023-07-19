import React from "react";
import './formlabel.css';
type FormInputProps = {
  for: string;
  text: string;
} & React.InputHTMLAttributes<HTMLInputElement>;

const FormLabel: React.FC<FormInputProps> = ({ htmlFor, text, ...rest }) => {
  return (
    <label htmlFor={htmlFor}>{text}</label>
  );
};

export default FormLabel;