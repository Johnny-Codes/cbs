import Button from "./Button";

const SubmitButton = ({ ...rest }) => {
  return (
    <Button
      type="cancel"
      buttonText="Cancel"
      {...rest}
      className="bg-red-300 hover:bg-red-500 text-black hover:text-white font-bold py-2 px-4 rounded m-4"
    />
  );
};

export default SubmitButton;
