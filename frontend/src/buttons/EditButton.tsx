import Button from "./Button";

const EditButton = ({ ...rest }) => {
  return (
    <Button
      type="edit"
      buttonText="Edit"
      {...rest}
      className="bg-green-300 hover:bg-green-500 text-white py-2 px-4 rounded m-4"
    />
  );
};

export default EditButton;
