import Button from "./Button";

const DeleteButton = ({ ...rest }) => {
  return (
    <Button
      type="button"
      buttonText="Delete"
      {...rest}
      className="bg-red-300 hover:bg-red-500 hover:text-white text-black font-bold py-2 px-4 rounded m-4"
    />
  );
};

export default DeleteButton;
