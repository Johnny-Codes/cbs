import React, { useState, useEffect } from "react";
import FormFields from "../forms/FormFields";
import GetCoinFamily from "./GetCoinFamily";
import GetCoinGrades from "./GetCoinGrades";
import GetCoinStrikes from "./GetCoinStrikes";
import GetCoinMints from "./GetCoinMints";
import GetCoinGradingServices from "./GetCoinGradingServices";
import SubmitButton from "../buttons/SubmitButton";
import CancelButton from "../buttons/CancelButton";
import "./AddCoinForm.css";
import { useSelector, useDispatch } from "react-redux";
import { changeBoolean } from "./addOrEditCoinSlice";
import GetCoinDetail from "./GetCoinDetail";
import { RootState } from "../store";

type CoinFormData = {
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
  denomination_of_coin: number;
  coin_type_name: number;
  grade: number;
  grade2?: number | null;
  strike: number;
  mint: number[];
  grading: number[];
};
const AddCoinForm = () => {
  const dispatch = useDispatch();
  const selId = useSelector((state: RootState) => state.selectedCoinId.id);

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
    denomination_of_coin: 0,
    coin_type_name: 0,
    grade: 0,
    grade2: null,
    strike: 0,
    mint: [],
    grading: [],
  });

  const initialFormData: CoinFormData = {
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
    denomination_of_coin: 0,
    coin_type_name: 0,
    grade: 0,
    grade2: null,
    strike: 0,
    mint: [],
    grading: [],
  };
  const [family, setFamily] = useState([]);
  const [denominations, setDenominations] = useState([]);
  const [coinName, setCoinName] = useState([]);
  const [coinGrades, setCoinGrades] = useState([]);
  const [coinStrikes, setCoinStrikes] = useState([]);
  const [coinMints, setCoinMints] = useState([]);
  const [coinGradingServices, setCoinGradingServices] = useState([]);

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

  const handleBulkCoins = () => {
    const grade2 = document.getElementById("grade2");
    const year2 = document.getElementById("year2");
    grade2?.classList.toggle("hidden");
    year2?.classList.toggle("hidden");
  };

  const handleFamilyChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedFamilyId = parseInt(e.target.value, 10);

    if (!selectedFamilyId) {
      setDenominations(0);
      setCoinName(0);
    } else {
      const selectedFamily = family.find(
        (item) => item.id === selectedFamilyId
      );
      setDenominations(selectedFamily.denominations);
    }
  };

  const handleDenominationChange = (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    const selectedDenominationId = parseInt(e.target.value, 10);

    if (!selectedDenominationId) {
      setCoinName(0);
    } else {
      const selectedDenomination = denominations.find(
        (item) => item.id === selectedDenominationId
      );
      setCoinName(selectedDenomination.coin_type_name);
    }
  };
  useEffect(() => {
    getRandomSku();
    GetCoinFamily(setFamily);
    GetCoinGrades(setCoinGrades);
    GetCoinStrikes(setCoinStrikes);
    GetCoinMints(setCoinMints);
    GetCoinGradingServices(setCoinGradingServices);

    GetCoinDetail(selId, setFormData, formData);
  }, []);

  const handleFormData = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    let newValue: string | number | number[] | boolean =
      type === "checkbox" ? checked : value;
    if (name === "mint") {
      const mintId = parseInt(value, 10);
      const updatedMints = checked
        ? [...formData.mint, mintId]
        : formData.mint.filter((id) => id !== mintId);
      newValue = updatedMints;
    }
    if (name === "grading") {
      const gradingId = parseInt(value, 10);
      const updatedGrading = checked
        ? [...formData.grading, gradingId]
        : formData.grading.filter((id) => id !== gradingId);
      newValue = updatedGrading;
    }

    setFormData({ ...formData, [name]: newValue });
    console.log("form data", formData);
  };

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const url = "http://localhost:8000/api/coins/";
    if (selId) {
      console.log("id exists?");
      // fuck, I need to return the full json from GetCoinDetail to do a PUT to /api/coins/id...
      // or do I? I have the ID for the URL. I need to get updated time from JS and
      // I can just PUT the formData and leave the rest alone...
      const date = Date.now();
      formData.updated_at = date;
      formData.id = selId;
      console.log("formData", formData);
      const fetchConfig = {
        method: "put",
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json",
        },
      };
      try {
        const response = await fetch(`${url}${selId}/`, fetchConfig);
        if (response.ok) {
          dispatch(changeBoolean());
        }
      } catch (error) {}
    } else {
      const fetchConfig = {
        method: "post",
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json",
        },
      };
      console.log("url", url, fetchConfig);
      try {
        const response = await fetch(url, fetchConfig);
        if (response.ok) {
          dispatch(changeBoolean());
        }
      } catch (error) {
        console.log("error", error);
      }
    }
  };

  const handleCancelForm = (e: React.FormEvent<HTMLFormElement>) => {
    dispatch(changeBoolean());
  };

  return (
    <>
      <h1>Add New Coin Inventory</h1>
      <form onSubmit={handleFormSubmit}>
        <FormFields
          labelText="Bulk?"
          htmlFor="is_bulk"
          value={formData.is_bulk}
          type="checkbox"
          name="is_bulk"
          onChange={handleFormData}
          onClick={handleBulkCoins}
          checked={formData.is_bulk}
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
          value={formData.pcgs_number}
        />
        <FormFields
          required
          labelText="Title"
          htmlFor="title"
          name="title"
          onChange={handleFormData}
          value={formData.title}
        />
        <FormFields
          required
          labelText="Year"
          type="number"
          htmlFor="year"
          name="year"
          onChange={handleFormData}
          value={formData.year}
        />
        <FormFields
          labelText="Year 2"
          htmlFor="year2"
          type="number"
          name="year2"
          onChange={handleFormData}
          className="hidden"
          value={formData.year2}
        />
        <FormFields
          labelText="Description"
          htmlFor="description"
          type="textarea"
          onChange={handleFormData}
          name="description"
          value={formData.description}
        />
        <FormFields
          required
          labelText="Cost"
          htmlFor="cost"
          type="number"
          onChange={handleFormData}
          name="cost"
          value={formData.cost}
        />
        <FormFields
          required
          labelText="Quantity"
          htmlFor="quantity"
          type="number"
          name="quantity"
          onChange={handleFormData}
          value={formData.quantity}
        />
        <FormFields
          labelText="Sale Price"
          htmlFor="sale_price"
          type="number"
          name="sale_price"
          onChange={handleFormData}
          value={formData.sale_price}
        />
        <div>
          <label htmlFor="family">Family</label>
          <select
            name="family_of_coin"
            onChange={(e) => {
              handleFormData(e);
              handleFamilyChange(e);
            }}
            required
            id="family"
            value={formData.family_of_coin}
          >
            <option value="">Select Family</option>
            {family &&
              family.map((family) => (
                <option key={family.id} value={family.id}>
                  {family.type}
                </option>
              ))}
          </select>
        </div>
        <div>
          <label htmlFor="denomination">Denomination</label>
          <select
            name="denomination_of_coin"
            onChange={(e) => {
              handleFormData(e);
              handleDenominationChange(e);
            }}
            required
            id="denomination"
            value={formData.denomination_of_coin}
          >
            <option value="">Select Denomination</option>
            {denominations &&
              denominations.map((denomination) => (
                <option key={denomination.id} value={denomination.id}>
                  {denomination.denomination_of_coin}
                </option>
              ))}
          </select>
        </div>
        <div>
          <label htmlFor="coin_name">Coin</label>
          <select
            required
            onChange={handleFormData}
            id="coin_name"
            name="coin_type"
          >
            <option value="">Select Coin</option>
            {coinName &&
              coinName.map((coin) => (
                <option key={coin.id} value={coin.id}>
                  {coin.coin_type}
                </option>
              ))}
          </select>
        </div>
        <div>
          <label htmlFor="grade">Grade</label>
          <select
            required
            onChange={handleFormData}
            id="grade"
            name="grade"
            value={formData.grade}
          >
            <option value="">Select Grade</option>
            {coinGrades &&
              coinGrades.map((coin) => (
                <option key={coin.id} value={coin.id}>
                  {coin.grade}
                </option>
              ))}
          </select>
        </div>
        <div>
          <label htmlFor="grade2" className="bulk">
            Grade 2
          </label>
          <select
            className="bulk hidden"
            onChange={handleFormData}
            id="grade2"
            name="grade2"
            value={formData.grade2}
          >
            <option value="">Select Grade</option>
            {coinGrades &&
              coinGrades
                .sort((a, b) => b.grade - a.grade)
                .map((coin) => (
                  <option key={coin.id} value={coin.id}>
                    {coin.grade}
                  </option>
                ))}
          </select>
        </div>
        <div>
          <label htmlFor="strike">Select Strike</label>
          <select
            required
            onChange={handleFormData}
            id="strike"
            name="strike"
            value={formData.strike}
          >
            <option value="">Select Strike</option>
            {coinStrikes &&
              coinStrikes.map((strike) => (
                <option key={strike.id} value={strike.id}>
                  {strike.strike}
                </option>
              ))}
          </select>
        </div>
        <div>
          {coinMints &&
            coinMints.map((mint) => {
              const isChecked = formData.mint.includes(mint.id);
              return (
                <FormFields
                  type="checkbox"
                  labelText={mint.coin_mint}
                  htmlFor={mint.id}
                  name="mint"
                  value={mint.id}
                  checked={isChecked}
                  onChange={handleFormData}
                  key={mint.id}
                />
              );
            })}
        </div>
        <div>
          {coinGradingServices &&
            coinGradingServices.map((service) => {
              const isChecked = formData.grading.includes(service.id);
              return (
                <FormFields
                  type="checkbox"
                  labelText={service.name}
                  htmlFor={service.id}
                  name="grading"
                  value={service.id}
                  checked={isChecked}
                  onChange={handleFormData}
                  key={service.id}
                />
              );
            })}
        </div>
        <span>
          <SubmitButton />
          <CancelButton onClick={handleCancelForm} />
        </span>
      </form>
    </>
  );
};

export default AddCoinForm;
