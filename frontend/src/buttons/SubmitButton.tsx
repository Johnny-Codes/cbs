import Button from "./Button";

const SubmitButton = ({ ...rest }) => {
  return <Button type="submit" buttonText="Submit" {...rest} />;
};

export default SubmitButton;