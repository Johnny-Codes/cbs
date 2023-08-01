import { useState, useEffect } from "react";
import FormFields from "../forms/FormFields";
import GetFamily from "./GetFamily";

interface CoinFormData {
  is_bulk: boolean;
  sku: string;
  pcgs_number?: number | null;
  title: string;
  year: number;
  year2?: number | null;
  description: string;
  cost: number;
  quantity: number;
  sale_price: number;
  family_of_coin: number;
}
const AddCoinForm = () => {
  const [formData, setFormData] = useState<CoinFormData>({
    is_bulk: false,
    sku: "",
    pcgs_number: null,
    title: "",
    year: 0,
    year2: null,
    description: "",
    cost: 0,
    quantity: 0,
    sale_price: 0,
    family_of_coin: 0,
  });

  const getRandomSku = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/sku/random/");
      if (response.ok) {
        const json = await response.json();
        const randomSku = json.random_sku;
        setFormData({ ...formData, sku: randomSku });
      }
    } catch (error) {
      console.log("error", error);
    }
  };

  const [family, setFamily] = useState([]);

  useEffect(() => {
    getRandomSku();
    GetFamily(setFamily);
  }, []);

  const handleFormData = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target);
    const { name, value, type, checked } = e.target;
    const newValue = type === "checkbox" ? checked : value;

    setFormData({ ...formData, [name]: newValue });
    console.log("form data", formData);
  };

  const handleFormSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("submit form data", formData);
  };

  return (
    <div className="form-container">
      <h1>Add New Coin Inventory</h1>
      <form onSubmit={handleFormSubmit}>
        <FormFields
          labelText="Bulk?"
          htmlFor="is_bulk"
          value={formData.is_bulk}
          type="checkbox"
          name="is_bulk"
          onChange={handleFormData}
        />
        <FormFields
          labelText="SKU"
          htmlFor="sku"
          type="text"
          name="sku"
          onChange={handleFormData}
          value={formData.sku}
        />
        <FormFields
          labelText="PCGS Number"
          htmlFor="pcgs_number"
          type="number"
          name="pcgs_number"
          onChange={handleFormData}
        />
        <FormFields
          required
          labelText="Title"
          htmlFor="title"
          name="title"
          onChange={handleFormData}
        />
        <FormFields
          required
          labelText="Year"
          type="number"
          htmlFor="year"
          name="year"
          onChange={handleFormData}
        />
        <FormFields
          labelText="Year 2"
          htmlFor="year2"
          type="number"
          name="year2"
          onChange={handleFormData}
        />
        <FormFields
          labelText="Description"
          htmlFor="description"
          type="textarea"
          onChange={handleFormData}
          name="description"
        />
        <FormFields
          required
          labelText="Cost"
          htmlFor="cost"
          type="number"
          onChange={handleFormData}
          name="cost"
        />
        <FormFields
          required
          labelText="Quantity"
          htmlFor="quantity"
          type="number"
          name="quantity"
          onChange={handleFormData}
        />
        <FormFields
          labelText="Sale Price"
          htmlFor="sale_price"
          type="number"
          name="sale_price"
          onChange={handleFormData}
        />
        <div>
          <select name="family_of_coin" onChange={handleFormData} required>
            <option value="">Select Family</option>
            {family.map((family) => (
              <option key={family.id} value={family.id}>
                {family.type}
              </option>
            ))}
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddCoinForm;
