import React, { useState, useEffect } from "react";
import EditButton from "../buttons/EditButton";
import { useGetAllActiveCustomersQuery } from "./api/customers";
import { selectedCustomerId } from "./customerSlice";
import { useDispatch } from "react-redux";
import DeleteButton from "../buttons/DeleteButton";
import { useSoftDeleteCustomerMutation } from "./api/customers";
import { useNavigate } from "react-router-dom";
import InvoiceButton from "../buttons/InvoiceButton";
import { addCustomerId } from "../salesinvoice/stores/salesCartSlice";

type customerType = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  state: string;
  business: string;
};

const CustomersList = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { data: customerData, isLoading: loadingCustomerData } =
    useGetAllActiveCustomersQuery(false);

  const [customers, setCustomers] = useState([]);
  const [deleteCustomer, deleteCustomerResponse] =
    useSoftDeleteCustomerMutation();

  useEffect(() => {
    if (customerData) {
      setCustomers(customerData);
    }
  }, [customerData]);

  if (loadingCustomerData) return <h1>Loading...</h1>;

  const handleEditCustomer = (e: React.ChangeEvent<HTMLInputElement>) => {
    dispatch(selectedCustomerId(e.target.value));
    navigate("/customers/add");
  };

  const handleDelete = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const id = e.target.value;
    deleteCustomer(id);
  };

  return (
    <div>
      <table className="table-auto border-collapse w-full">
        <thead>
          <tr className="bg-blue-500">
            <th className="border border-black p-2">Name</th>
            <th className="border border-black p-2">Phone Number</th>
            <th className="border border-black p-2">Email</th>
            <th className="border border-black p-2">State</th>
            <th className="border border-black p-2">Wholesale</th>
            <th className="border border-black p-2">Edit</th>
          </tr>
        </thead>
        <tbody>
          {customers &&
            customers.map((customer: customerType) => (
              <tr key={customer.id} className="even:bg-blue-200">
                <td className="border border-black p-2">
                  {customer.first_name} {customer.last_name}
                </td>
                <td className="border border-black p-2">
                  {customer.phone_number}
                </td>
                <td className="border border-black p-2">{customer.email}</td>
                <td className="border border-black p-2">{customer.state}</td>
                <td className="border border-black p-2">
                  {customer.business ? <>{customer.business}</> : "No"}
                </td>
                <td className="border border-black p-2">
                  <EditButton
                    value={customer.id}
                    onClick={(e) => {
                      handleEditCustomer(e);
                    }}
                  />
                  <DeleteButton
                    id={customer.id}
                    value={customer.id}
                    onClick={handleDelete}
                  />
                  <InvoiceButton
                    id={customer.id}
                    value={customer.id}
                    onClick={() => dispatch(addCustomerId(1))}
                  />
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomersList;
