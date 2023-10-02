import { useState } from "react";
import SalesCart from "./SalesCart";
import SalesInvoice from "./SalesInvoice";
import SalesCustomer from "./SalesCustomer";
import SalesNotes from "./SalesNotes";

const SalesInvoicePage = () => {
  const [componentSelector, setComponentSelector] = useState("SalesInvoice");
  return (
    <>
      <div className="grid grid-cols-12 m-4">
        <div className="col-span-3 p-4">
          <span
            className="hover:cursor-pointer bg-slate-300 rounded p-4"
            onClick={() => setComponentSelector("SalesInvoice")}
          >
            Add Items
          </span>
        </div>
        <div className="col-span-3 p-4">
          <span
            className="hover:cursor-pointer bg-slate-300 rounded p-4"
            onClick={() => setComponentSelector("AddSalesCustomer")}
          >
            Add Customer
          </span>
        </div>
        <div className="col-span-3 p-4">
          <span
            className="hover:cursor-pointer bg-slate-300 rounded p-4"
            onClick={() => setComponentSelector("SalesNotes")}
          >
            Add Notes
          </span>
        </div>
      </div>
      <hr></hr>
      <div className="grid grid-cols-12">
        <div className="col-span-9">
          {componentSelector === "SalesInvoice" ? (
            <SalesInvoice />
          ) : componentSelector === "AddSalesCustomer" ? (
            <SalesCustomer />
          ) : componentSelector === "SalesNotes" ? (
            <SalesNotes />
          ) : null}
        </div>
        <div className="col-span-3">
          <SalesCart />
        </div>
      </div>
    </>
  );
};

export default SalesInvoicePage;
