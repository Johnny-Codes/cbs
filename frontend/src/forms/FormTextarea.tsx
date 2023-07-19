import React from "react";

type FormTextareaProps = {
  type: string;
} & React.InputHTMLAttributes<HTMLInputElement>;

const FormTextarea: React.FC<FormTextareaProps> = ({ id, ...rest }) => {
  return (
    <textarea id={id} {...rest} />
  );
};

export default FormTextarea;