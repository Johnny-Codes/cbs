import EditButton from "../buttons/EditButton";
import { useGetAllCustomersQuery } from "./services/customers";

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
  const { data: customers } = useGetAllCustomersQuery("");
  console.log(customers);

  return (
    <>
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
                    onClick={() => {
                      console.log(customer.id);
                    }}
                  />
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </>
  );
};

export default CustomersList;
