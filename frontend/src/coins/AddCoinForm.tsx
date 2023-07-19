import { useState, useEffect } from "react";
import axios from "axios";
import FormButton from "../buttons/FormButton";
import FormInput from "../forms/FormInput";
import FormLabel from "../forms/FormLabel";
import FormTextarea from "../forms/FormTextarea";
import FormCheckbox from "../forms/FormCheckbox";

const AddCoinForm: React.FC = () => {
  const [bulk, setBulk] = useState(false);
  const [sku, setSKU] = useState("");
  const [pcgsNumber, setPCGSNumber] = useState();
  const [year, setYear] = useState();
  const [year2, setYear2] = useState();
  const [family, setFamily] = useState();
  const [denom, setDenom] = useState();
  const [coinType, setCoinType] = useState();
  const [familyOptions, setFamilyOptions] = useState([]);
  const [denominationOptions, setDenominationOptions] = useState([]);
  const [coinTypeOptions, setCoinTypeOptions] = useState([]);
  const [description, setDescription] = useState([]);
  const [cost, setCost] = useState();
  const [quantity, setQuantity] = useState();
  const [mints, setMints] = useState([]);
  const [selectedMints, setSelectedMints] = useState([]);
  const [grading, setGrading] = useState([]);
  const [selectedServices, setSelectedServices] = useState([]);
  const [allGrades, setAllGrades] = useState([]);
  const [grade, setGrade] = useState([]);
  const [grade2, setGrade2] = useState();
  const [salePrice, setSalePrice] = useState();
  const [strikes, setStrikes] = useState([]);
  const [strike, setStrike] = useState();
  const [title, setTitle] = useState();

  const bulkItems = document.querySelectorAll(".bulk");
  const bulkChange = (e) => {
    setBulk(!bulk);
    bulkItems?.forEach((item) => {
      item.classList.toggle("hidden");
    });
  };

  const handleChanges = (e, setState) => {
    const data = e.target.value;
    console.log("handleChanges", data);
    setState(data);
  };

  const familyChange = (e) => {
    const data = e.target.value;
    setFamily(data);
  };

  const denomChange = (e) => {
    const data = e.target.value;
    setDenom(data);
  };

  const coinChange = (e) => {
    const data = e.target.value;
    setCoinType(data);
  };

  const descriptionChange = (e) => {
    const data = e.target.value;
    setDescription(data);
  };

  const handleStrikeChange = (e) => {
    const data = e.target.value;
    setStrike(data);
  };

  const gradingChange = (e) => {
    const serviceId = parseInt(e.target.value);
    const checked = e.target.checked;

    if (checked) {
      setSelectedServices((prevSelectedServices) => [
        ...prevSelectedServices,
        serviceId,
      ]);
    } else {
      setSelectedServices((prevSelectedServices) =>
        prevSelectedServices.filter((id) => id !== serviceId)
      );
    }
  };

  const mintChange = (e) => {
    const mintId = parseInt(e.target.value);
    const checked = e.target.checked;
    console.log("mint id", mintId);

    if (checked) {
      setSelectedMints((prevSelectedMints) => [...prevSelectedMints, mintId]);
    } else {
      setSelectedMints((prevSelectedMints) =>
        prevSelectedMints.filter((id) => id !== mintId)
      );
    }
  };

  const handleFamilyChange = (e) => {
    const id = e.target.value;
    for (let coins of familyOptions) {
      if (coins.id == id) {
        let denom = coins.denominations;
        setDenominationOptions(denom);
        break;
      }
    }
  };

  const handleDenominationChange = (e) => {
    const id = e.target.value;
    for (let type of denominationOptions) {
      if (type.id == id) {
        let types = type.coin_type_name;
        setCoinTypeOptions(types);
        break;
      }
    }
  };

  const handleGradeChange = (e) => {
    const data = e.target.value;
    setGrade(data);
  };

  const handleGrade2Change = (e) => {
    const data = e.target.value;
    setGrade2(data);
  };

  const getFamilyData = () => {
    axios
      .get("http://localhost:8000/api/coins/family/")
      .then((response) => {
        setFamilyOptions(response.data);
      })
      .catch((error) => {
        console.error("Error fetching family options:", error);
      });
  };

  const getMints = () => {
    axios
      .get("http://localhost:8000/api/coins/mints/")
      .then((response) => {
        setMints(response.data);
      })
      .catch((error) => {
        console.error("Error fetching Mints", error);
      });
  };

  const getGradingServices = () => {
    axios
      .get("http://localhost:8000/api/coins/gradingservices/")
      .then((response) => {
        setGrading(response.data);
      })
      .catch((error) => {
        console.log("Error fetching grading services", error);
      });
  };

  const getGrades = () => {
    axios
      .get("http://localhost:8000/api/coins/coingrades/")
      .then((response) => {
        setAllGrades(response.data);
      })
      .catch((error) => {
        console.log("Error fetching coin grades", error);
      });
  };

  const getStrikes = () => {
    axios
      .get("http://localhost:8000/api/coins/strike")
      .then((response) => {
        setStrikes(response.data);
      })
      .catch((error) => {
        console.log("Error fetching Strikes", error);
      });
  };

  const getRandomSku = () => {
    axios
      .get("http://localhost:8000/api/sku/random")
      .then((response) => {
        setSKU(response.data.random_sku);
      })
      .catch((error) => {
        console.log("Error fetching random SKU");
      });
  };

  useEffect(() => {
    getFamilyData();
    getMints();
    getGradingServices();
    getGrades();
    getStrikes();
    getRandomSku();
  }, []);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = {};
    form.sku = sku;
    form.is_bulk = bulk;
    form.pcgs_number = Number(pcgsNumber);
    form.year = Number(year);
    form.year2 = Number(year2);
    form.family_of_coin = Number(family);
    form.denomination_of_coin = Number(denom);
    form.coin_type = Number(coinType);
    form.description = description;
    form.cost = cost;
    form.quantity = Number(quantity);
    form.mint = selectedMints;
    form.grading = selectedServices;
    form.grade = Number(grade);
    form.grade2 = Number(grade2);
    form.title = title;
    form.strike = Number(strike);
    form.sale_price = salePrice;
    axios.post("http://localhost:8000/api/coins/", form).catch((error) => {
      console.log("error posting coin", error);
      console.log("error data", error.response.data);
      console.log("error status", error.response.status);
      console.log("error statustext", error.response.statusText);
      console.log("error headers", error.response.headers);
    });
  };

  return (
    <div className="form-container">
      <h1>Add New Coin Inventory</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <FormCheckbox
            labelText="Bulk"
            name="is_bulk"
            id="is_bulk"
            onChange={bulkChange}
          />
        </div>
        <div>
          <FormLabel htmlFor="sku" text="SKU" />
          <FormInput
            required
            type="text"
            name="sku"
            id="sku"
            value={sku}
            onChange={(e) => handleChanges(e, setSKU)}
          />
        </div>
        <div>
          <FormLabel htmlFor="pcgs_number" text="PCGS Number" />
          <FormInput
            type="number"
            name="pcgs_number"
            id="pcgs_number"
            onChange={(e) => handleChanges(e, setPCGSNumber)}
          />
        </div>
        <div>
          <FormLabel htmlFor="title" text="Title" />
          <FormInput
            type="text"
            name="title"
            id="title"
            required
            onChange={(e) => handleChanges(e, setTitle)}
          />
        </div>
        <div>
          <FormLabel htmlForm="year" text="Year" />
          <FormInput
            type="number"
            required
            name="year"
            id="year"
            onChange={(e) => handleChanges(e, setYear)}
          />
        </div>
        <div className="bulk hidden">
          <FormLabel htmlForm="year2" text="Year 2" />
          <FormInput
            type="number"
            name="year2"
            id="year2"
            onChange={(e) => handleChanges(e, setYear2)}
          />
        </div>
        <div>
          <FormLabel htmlFor="grading-service" text="Grading Service" />
          {grading.map((service) => (
            <div key={service.id}>
              <FormCheckbox
                labelText={service.name}
                id={`service-${service.id}`}
                value={service.id}
                checked={selectedServices.includes(service.id)}
                onChange={gradingChange}
              />
            </div>
          ))}
        </div>
        <div>
          <FormLabel htmlFor="grade" text="Grade" />
          <select name="grade" id="grade" onChange={handleGradeChange}>
            <option value="">Select Grade</option>
            {allGrades.map((grade) => (
              <option key={grade.id} value={grade.id}>
                {grade.grade}
              </option>
            ))}
          </select>
        </div>
        <div className="bulk hidden">
          <FormLabel htmlFor="grade2" text="Grade 2" />
          <select name="grade2" id="grade2" onChange={handleGrade2Change}>
            <option value="">Select Grade</option>
            {allGrades.map((grade) => (
              <option key={grade.id} value={grade.id}>
                {grade.grade}
              </option>
            ))}
          </select>
        </div>
        <div>
          <FormLabel htmlFor="strike" text="Strike" />
          <select name="strike" id="strike" onChange={handleStrikeChange}>
            <option value="">Select Strike</option>
            {strikes.map((s) => (
              <option key={s.id} value={s.id}>
                {s.strike}
              </option>
            ))}
          </select>
        </div>
        <div>
          <FormLabel htmlFor="family_of_coin" text="Family" />
          <select
            required
            name="family_of_coin"
            id="family_of_coin"
            onChange={(e) => {
              handleFamilyChange(e);
              familyChange(e);
            }}
          >
            <option value="">Select</option>
            {familyOptions.map((family) => (
              <option key={family.id} value={family.id}>
                {family.type}
              </option>
            ))}
          </select>
        </div>
        <div>
          <FormLabel htmlFor="denomination_of_coin" text="Denomination" />
          <select
            required
            name="denomination_of_coin"
            id="denomination_of_coin"
            onChange={(e) => {
              handleDenominationChange(e);
              denomChange(e);
            }}
          >
            <option value="">Select</option>
            {denominationOptions.map((denom) => (
              <option key={denom.id} value={denom.id}>
                {denom.denomination_of_coin}
              </option>
            ))}
            ;
          </select>
        </div>
        <div>
          <FormLabel htmlFor="coin_type" text="Coin Name" />
          <select
            required
            name="coin_type"
            id="coin_type"
            onChange={coinChange}
          >
            <option value="">Select</option>
            {coinTypeOptions.map((type) => (
              <option key={type.id} value={type.id}>
                {type.coin_type}
              </option>
            ))}
          </select>
        </div>
        <div>
          <FormLabel htmlFor="description" text="Description" />
          <FormTextarea
            id="description"
            name="description"
            cols="30"
            rows="10"
            onChange={(e) => handleChanges(e, setDescription)}
          />
        </div>
        <div>
          <FormLabel htmlFor="cost" text="Cost" />
          <FormInput
            type="number"
            step="0.01"
            name="cost"
            id="cost"
            onChange={(e) => handleChanges(e, setCost)}
          />
        </div>
        <div>
          <FormLabel htmlFor="quantity" text="Quantity" />
          <FormInput
            type="number"
            required
            name="quantity"
            id="quantity"
            onChange={(e) => handleChanges(e, setQuantity)}
          />
        </div>
        <div>
          <FormLabel htmlFor="sale_price" text="Sale Price" />
          <FormInput
            type="number"
            step="0.01"
            name="sale_price"
            id="sale_price"
            onChange={(e) => handleChanges(e, setSalePrice)}
          />
        </div>
        <div>
          <FormLabel htmlFor="mints" text="Mint" />
          {mints.map((mint) => (
            <div key={mint.id}>
              <FormCheckbox
                id={`mint-${mint.id}`}
                labelText={mint.coin_mint}
                value={mint.id}
                checked={selectedMints.includes(mint.id)}
                onChange={mintChange}
              />
            </div>
          ))}
        </div>
        <div><FormButton text="Submit" /></div>
        
      </form>
    </div>
  );
};

export default AddCoinForm;
