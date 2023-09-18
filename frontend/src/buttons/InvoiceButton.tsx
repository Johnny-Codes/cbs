import Button from "./Button";

const InvoiceButton = ({ ...rest }) => {
  return (
    <Button
      type="submit"
      buttonText="Invoice"
      {...rest}
      className="bg-green-300 hover:bg-slate-300 text-black hover:text-white font-bold py-2 px-4 rounded m-4"
    />
  );
};

export default InvoiceButton;
