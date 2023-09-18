import { useState, useEffect } from "react";
import { useGetAllCustomersQuery } from "../customers/api/customers";
import FormFields from "../forms/FormFields";
import InvoiceButton from "../buttons/InvoiceButton";
import { useDispatch } from "react-redux";
import { addCustomerId } from "./stores/salesCartSlice";

const SalesCustomer = () => {
  const { data: allCustomers, isLoading: allCustomersLoading } =
    useGetAllCustomersQuery("");
  const [customers, setCustomers] = useState();
  const [searchLastName, setSearchLastName] = useState("");
  const [filteredCustomers, setFilteredCustomers] = useState();
  const dispatch = useDispatch();
  useEffect(() => {
    if (allCustomers) {
      setCustomers(allCustomers);
    }
  }, [allCustomers, setCustomers]);
  if (allCustomersLoading) return <h1>Loading...</h1>;

  const handleSearchLastName = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setSearchLastName(e.target.value);
    const filtered = allCustomers.filter((customer) =>
      customer.last_name.toLowerCase().includes(e.target.value.toLowerCase())
    );
    setFilteredCustomers(filtered);
  };

  const handleAddCustomerToInvoice = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    dispatch(addCustomerId(e.target.value));
  };

  return (
    <div>
      <h1>Sales Customer</h1>
      <FormFields
        htmlFor="last_name"
        type="text"
        name="last_name"
        labelText="Search Last Name"
        onChange={(e) => handleSearchLastName(e)}
      />
      {filteredCustomers?.map((customer) => (
        <div
          key={customer.id}
          value={customer.id}
          className="even:bg-slate-200 odd:bg-slate-400 p-2"
        >
          {customer.first_name} {customer.last_name}{" "}
          <InvoiceButton
            id={customer.id}
            value={customer.id}
            onClick={(e) => handleAddCustomerToInvoice(e)}
          />
        </div>
      ))}
    </div>
  );
};

export default SalesCustomer;
