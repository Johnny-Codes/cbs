import { useState, useEffect } from "react";
import axios from "axios";

interface CoinFormData {
  pcgs_number: number;
  title: string;
  year: number;
  year2: number | null;
  description: string;
  cost: string;
  quantity: number;
  sale_price: number | null;
  mint: number[];
  family_of_coin: number;
  denomination_of_coin: number;
  coin_type: number;
  grading: number;
  grade: number;
  grade2: number | null;
  images: number[];
  strike: number;
  bulk: boolean;
}

const App: React.FC = () => {
  const [formData, setFormData] = useState<CoinFormData>({});
  const [bulk, setBulk] = useState(false);
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
  const [quantity, setQuantity] = useState(1);
  const [mints, setMints] = useState([]);
  const [selectedMints, setSelectedMints] = useState([]);
  const [grading, setGrading] = useState([]);
  const [selectedServices, setSelectedServices] = useState([])

 

  const bulkItems = document.querySelectorAll('.bulk')
  const bulkChange = (e) => {
    setBulk(!bulk)
    bulkItems?.forEach((item) => {item.classList.toggle('hidden')})
  }
  const PCGSChange = (e) => {
    const data = e.target.value;
    setPCGSNumber(data);
  };

  const yearChange = (e) => {
    const data = e.target.value;
    setYear(data);
  };

  const year2Change = (e) => {
    const data = e.target.value;
    setYear2(data);
  }

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
  }

  const costChange = (e) => {
    const data = e.target.value;
    setCost(data);
  }

  const quantityChange = (e) => {
    const data = e.target.value;
    setQuantity(data);
  }

  const gradingChange = (e) => {
    const serviceId = parseInt(e.target.value);
    const checked = e.target.checked;
  
    if (checked) {
      setSelectedServices((prevSelectedServices) => [...prevSelectedServices, serviceId]);
    } else {
      setSelectedServices((prevSelectedServices) =>
        prevSelectedServices.filter((id) => id !== serviceId)
      );
    }
  };

  const mintChange = (e) => {
    const mintId = parseInt(e.target.value);
    const checked = e.target.checked;
  
    if (checked) {
      setSelectedMints((prevSelectedMints) => [...prevSelectedMints, mintId]);
    } else {
      setSelectedMints((prevSelectedMints) =>
        prevSelectedMints.filter((id) => id !== mintId)
      );
    }
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

  const getMints = () => {
    axios.get('http://localhost:8000/api/coins/mints/')
    .then((response) => {
      setMints(response.data);
    })
    .catch((error) => {
      console.error("Error fetching Mints", error)
    })
  }

  const getGradingServices = () => {
    axios.get('http://localhost:8000/api/coins/gradingservices/')
    .then((response) => {setGrading(response.data);
    })
    .catch((error) => {
      console.log("Error fetching grading services", error);
    })
  }

  useEffect(() => {
    getFamilyData();
    getMints();
    getGradingServices();
  }, []);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = {};
    form.is_bulk = bulk;
    form.pcgs_number = pcgsNumber;
    form.year = year;
    form.year2 = year2;
    form.family_of_coin = family;
    form.denomination_of_coin = denom;
    form.coin_type = coinType;
    form.description = description;
    form.cost = cost;
    form.quantity = quantity;
    form.mint = selectedMints;
    form.grading = selectedServices;
    // axios
    //   .post("http://localhost:8000/api/coins/", formData)
    //   .then((response) => {console.log(response.data)})
    //   .catch((error) => {console.log(error);});
    const json = JSON.stringify(form);
    console.log("submitted");
    console.log(form);
  };

  return (
    <>
      <h1>Add New Coin Inventory</h1>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="is_bulk">Bulk</label>
          <input type="checkbox" name="is_bulk" id="is_bulk" onChange={bulkChange}/>
        </div>
        <div>
          <label htmlFor="pcgs_number">PCGS Number</label>
          <input
            type="number"
            name="pcgs_number"
            id="pcgs_number"
            onChange={PCGSChange}
          />
        </div>
        <div>
          <label htmlFor="grading-service">Grading Service</label>
          {grading.map((service) => (
            <div key={service.id}>
              <input 
                type="checkbox" 
                id={`service-${service.id}`} 
                value={service.id} 
                checked={selectedServices.includes(service.id)} 
                onChange={gradingChange}
                />
              <label htmlFor={`service-${service.id}`}>{service.name}</label>
            </div>
          ))}
        </div>
        <div>
          <label htmlFor="year">Year</label>
          <input
            required
            type="number"
            name="year"
            id="year"
            onChange={yearChange}
          />
        </div>
        <div className="bulk hidden">
          <label htmlFor="year2">Year 2</label>
          <input type="number" name="year2" id="year2" onChange={year2Change}/>
        </div>
        <div>
          <label htmlFor="family_of_coin">Family</label>
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
          <label htmlFor="denomination_of_coin">Denomination</label>
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
          <label htmlFor="coin_type">Coin Name</label>
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
          <label htmlFor="description">Description</label>
          <textarea name="description" id="description" cols="30" rows="10" onChange={descriptionChange}/>
        </div>
        <div>
          <label htmlFor="cost">Cost</label>
          <input type="number" name="cost" id="cost" onChange={costChange}/>
        </div>
        <div>
          <label htmlFor="quantity">Quantity</label>
          <input type="number" name="quantity" id="quantity" onChange={quantityChange}/>
        </div>
        <div>
          <label htmlFor="mints">Mint</label>
          {mints.map((mint) => (
            <div key={mint.id}>
              <input
                type="checkbox"
                id={`mint-${mint.id}`}
                value={mint.id}
                checked={selectedMints.includes(mint.id)}
                onChange={mintChange}
              />
              <label htmlFor={`mint-${mint.id}`}>{mint.coin_mint}</label>
            </div>
          ))}
        </div>
        <div>
          <button>Submit</button>
        </div>
      </form>
    </>
  );
};

export default App;
