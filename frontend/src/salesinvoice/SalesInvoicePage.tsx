import SalesCart from "./SalesCart";
import SalesInvoice from "./SalesInvoice";

const SalesInvoicePage = () => {
  return (
    <div className="grid grid-cols-12">
      <div className="col-span-9">
        <SalesInvoice />
      </div>
      <div className="col-span-3">
        <SalesCart />
      </div>
    </div>
  );
};

export default SalesInvoicePage;
