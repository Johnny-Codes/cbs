import React, { useState, useEffect } from "react";
import EditButton from "../buttons/EditButton";
import {
  useGetAllCustomersQuery,
  useGetCustomerDetailQuery,
} from "./services/customers";
import { selectedCustomerId } from "./customerSlice";
import AddOrEditCustomer from "./AddOrEditCustomer";
import Button from "../buttons/Button";
import { useSelector, useDispatch } from "react-redux";

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
  const dispatch = useDispatch();
  const { data: customerData, isLoading: loadingCustomerData } =
    useGetAllCustomersQuery("");

  const selectedCustomer = useSelector(
    (state: RootState) => state.selectedCustomerId.id
  );

  const [customers, setCustomers] = useState([]);

  const [addCustomer, setAddCustomer] = useState(false);

  useEffect(() => {
    if (customerData) {
      setCustomers(customerData);
    }
  }, [customerData]);

  if (loadingCustomerData) return <h1>Loading...</h1>;

  const handleEditCustomer = (e) => {
    console.log(e.target.value);
    dispatch(selectedCustomerId(e.target.value));
  };

  return (
    <div>
      <Button
        buttonText="Add Customer"
        type="button"
        className="border p-4"
        onClick={(e) => {
          setAddCustomer(true);
          handleEditCustomer(e);
        }}
      />
      {addCustomer && <AddOrEditCustomer />}
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
              <tr key={customer.id}>
                <td className="border border-black p-2">
                  {customer.first_name} {customer.last_name}
                </td>
                <td className="border border-black p-2">
                  {customer.phone_number}
                </td>
                <td className="border border-black p-2">{customer.email}</td>
                <td className="border border-black p-2">{customer.state}</td>
                <td className="border border-black p-2">
                  {customer.business ? <>"Yes" {customer.business}</> : "No"}
                </td>
                <td className="border border-black p-2">
                  <EditButton
                    value={customer.id}
                    onClick={(e) => {
                      setAddCustomer(true), handleEditCustomer(e);
                    }}
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
