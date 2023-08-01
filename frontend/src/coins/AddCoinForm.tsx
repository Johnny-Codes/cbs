import { useState, useEffect } from "react";
import FormInput from "../forms/FormInput";
import FormLabel from "../forms/FormLabel";

interface CoinFormData {
  is_bulk: boolean;
  sku: string;
  pcgs_number: number | null;
  title: string;
  year: number;
  year2?: number | null;
}
const AddCoinForm = () => {
  const [formData, setFormData] = useState<CoinFormData>({
    is_bulk: false,
    sku: "",
    pcgs_number: null,
    title: "",
    year: 0,
    year2: null,
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

  useEffect(() => {
    getRandomSku();
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
        <div>
          <FormLabel text="Bulk?" htmlFor="is_bulk" />
          <FormInput
            value={formData.is_bulk}
            type="checkbox"
            name="is_bulk"
            id="is_bulk"
            onChange={handleFormData}
          />
        </div>
        <div>
          <FormLabel text="SKU" htmlFor="sku" />
          <FormInput
            required
            id="sku"
            type="string"
            name="sku"
            onChange={handleFormData}
            value={formData.sku}
          />
        </div>
        <div>
          <FormLabel text="PCGS Number" htmlFor="pcgs_number" />
          <FormInput
            id="pcgs_number"
            type="number"
            name="pcgs_number"
            onChange={handleFormData}
          />
        </div>
        <div>
          <FormLabel text="Title" htmlFor="title" />
          <FormInput
            required
            id="title"
            name="title"
            value={formData.title}
            type="text"
            onChange={handleFormData}
          />
        </div>
        <div>
          <FormLabel text="Year" htmlFor="year" />
          <FormInput
            required
            type="number"
            id="year"
            name="year"
            onChange={handleFormData}
          />
        </div>
        <div>
          <FormLabel text="Year 2" htmlFor="year2" />
          <FormInput
            type="number"
            id="year2"
            name="year2"
            onChange={handleFormData}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddCoinForm;
