import { useState, useEffect } from "react";
import { useGetAllCoinsQuery } from "../coins/services/coins";
import FormFields from "../forms/FormFields";
import SearchCoinsModal from "../coins/SearchCoinsModal";

const SalesInvoice = () => {
  const { data: allCoinsData, isLoading: allCoinsDataLoading } =
    useGetAllCoinsQuery("");
  const [allCoins, setAllCoins] = useState({});
  const [formData, setFormData] = useState({});
  const [selectedSku, setSelectedSku] = useState("");
  const [isNewSku, setIsNewSku] = useState(false);
  const [isSearchCoinsOpen, setIsSearchCoinsOpen] = useState(false);

  const openSearchCoins = () => {
    setIsSearchCoinsOpen(true);
  };
  const closeSearchCoins = () => {
    setIsSearchCoinsOpen(false);
  };

  useEffect(() => {
    if (!allCoinsDataLoading) {
      console.log("use effect");
      setAllCoins(allCoinsData);
    }
  }, [allCoinsDataLoading]);

  if (allCoinsDataLoading) return <h1>Loading</h1>;

  const handleSkuChange = (e) => {
    const inputSku = e.target.value;
    setSelectedSku(inputSku);
    setIsNewSku(!allCoins.some((coin) => coin.sku === inputSku));
  };

  return (
    <div>
      <form>
        <FormFields
          htmlFor="sku"
          type="text"
          name="sku"
          placeholder="SKU"
          onChange={handleSkuChange}
          value={selectedSku}
        />
      </form>
      <div>
        <button onClick={openSearchCoins}>Open Modal</button>
        <SearchCoinsModal
          isOpen={isSearchCoinsOpen}
          onClose={closeSearchCoins}
        />
      </div>
    </div>
  );
};

export default SalesInvoice;
