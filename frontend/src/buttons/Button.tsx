type ButtonType = {
  buttonText: string;
  type: string;
};

const Button = ({ buttonText, type, ...rest }: ButtonType) => {
  return (
    <button type={type} {...rest}>
      {buttonText}
    </button>
  );
};

export default Button;
