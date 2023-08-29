import { useState, useEffect } from "react";
import {
  useAddCustomerMutation,
  useGetCustomerDetailQuery,
  useSoftDeleteCustomerMutation,
} from "./services/customers";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../store";

import FormFields from "../forms/FormFields";
import SubmitButton from "../buttons/SubmitButton";
import CancelButton from "../buttons/CancelButton";
import DeleteButton from "../buttons/DeleteButton";
import { selectedCustomerId } from "./customerSlice";

import { useNavigate } from "react-router-dom";

type formData = {
  first_name: string;
  last_name: string;
  email: string;
  address_1: string;
  address_2: string;
  city: string;
  state: string;
  zip_code: string;
};

const AddOrEditCustomer = () => {
  const [formData, setFormData] = useState<formData>({
    first_name: "",
    last_name: "",
    email: "",
    address_1: "",
    address_2: "",
    city: "",
    state: "",
    zip_code: "",
  });

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const customerId = useSelector(
    (state: RootState) => state.selectedCustomerId.id
  );

  const { data: customerData, isLoading: loadingCustomerData } =
    useGetCustomerDetailQuery(customerId);

  useEffect(() => {
    if (customerData) {
      setFormData(customerData);
    }
  }, [customerData]);

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const [addCustomer, addCustomerResponse] = useAddCustomerMutation();
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!customerId) {
      addCustomer({ data: formData, id: "", method: "POST" });
    } else {
      addCustomer({ data: formData, id: formData.id, method: "PUT" });
    }
    dispatch(selectedCustomerId(null));
    navigate("/customers");
  };

  const [deleteCustomer, deleteCustomerResponse] =
    useSoftDeleteCustomerMutation();

  const handleDelete = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const id = formData.id;
    deleteCustomer(id);
    navigate("/customers");
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <FormFields
          labelText="First Name"
          htmlFor="first_name"
          value={formData.first_name}
          type="text"
          name="first_name"
          onChange={handleFormChange}
          placeholder="First Name"
        />
        <FormFields
          labelText="Last Name"
          htmlFor="last_name"
          value={formData.last_name}
          type="text"
          name="last_name"
          onChange={handleFormChange}
          placeholder="Last Name"
        />
        <FormFields
          labelText="Email"
          htmlFor="email"
          value={formData.email}
          type="text"
          name="email"
          onChange={handleFormChange}
          placeholder="email"
        />
      </div>

      <div>
        <FormFields
          labelText="Address Line 1"
          htmlFor="address_1"
          value={formData.address_1}
          type="text"
          name="address_1"
          onChange={handleFormChange}
          placeholder="Address Line 1"
        />
        <FormFields
          labelText="Address Line 2"
          htmlFor="address_2"
          value={formData.address_2}
          type="text"
          name="address_2"
          onChange={handleFormChange}
          placeholder="Address Line 2"
        />
        <FormFields
          labelText="City"
          htmlFor="city"
          value={formData.city}
          type="text"
          name="city"
          onChange={handleFormChange}
          placeholder="City"
        />
        <FormFields
          labelText="State"
          htmlFor="state"
          value={formData.state}
          type="text"
          name="state"
          onChange={handleFormChange}
          placeholder="State"
        />
        <FormFields
          labelText="Zip Code"
          htmlFor="zip_code"
          value={formData.zip_code}
          type="text"
          name="zip_code"
          onChange={handleFormChange}
          placeholder="Zip Code"
        />
      </div>
      <div>
        <SubmitButton />
        <DeleteButton
          id={customerId}
          value={customerId}
          onClick={handleDelete}
        />
        <CancelButton
          onClick={() => {
            navigate("/customers"), dispatch(selectedCustomerId(null));
          }}
        />
      </div>
    </form>
  );
};

export default AddOrEditCustomer;
