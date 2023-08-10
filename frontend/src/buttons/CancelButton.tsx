import Button from "./Button";

const SubmitButton = ({ ...rest }) => {
  return <Button type="cancel" buttonText="Cancel" {...rest} />;
};

export default SubmitButton;
