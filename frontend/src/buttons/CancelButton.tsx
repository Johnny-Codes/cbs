import Button from "./Button";

const CancelButton = ({ ...rest }) => {
  return (
    <Button
      type="button"
      buttonText="Cancel"
      {...rest}
      className="bg-gray-300 hover:bg-gray-500 text-black hover:text-white font-bold py-2 px-4 rounded m-4"
    />
  );
};

export default CancelButton;
