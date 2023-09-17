import { useState, useEffect } from "react";
import { useGetAllCustomersQuery } from "../customers/api/customers";

const SalesCustomer = () => {
  const { data: allCustomers, isLoading: allCustomersLoading } =
    useGetAllCustomersQuery("");
  const [customers, setCustomers] = useState();

  useEffect(() => {
    if (allCustomers) {
      setCustomers(allCustomers);
    }
  }, [allCustomers, setCustomers]);
  if (allCustomersLoading) return <h1>Loading...</h1>;
  console.log("all customers", allCustomers);

  return (
    <div>
      <h1>Sales Customer</h1>
      {customers?.map((customer) => (
        <div key={customer.id}>
          {customer.first_name} {customer.last_name}
        </div>
      ))}
    </div>
  );
};

export default SalesCustomer;
