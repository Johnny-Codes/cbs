import { useState, useEffect } from "react";
import { useGetAllCoinsQuery } from "../coins/services/coins";
import FormFields from "../forms/FormFields";
import FormTextarea from "../forms/FormTextarea";
import SearchCoinsModal from "../coins/SearchCoinsModal";
import { RootState } from "../store";
import { useDispatch, useSelector } from "react-redux";
import { addToCart } from "./stores/salesCartSlice";
import { HiOutlineShoppingCart } from "react-icons/hi2";

type SkuProps = {
  sku: string;
};

const SalesInvoice = () => {
  const dispatch = useDispatch();
  const { data: allCoinsData, isLoading: allCoinsDataLoading } =
    useGetAllCoinsQuery("");
  const [allCoins, setAllCoins] = useState({});
  const [skuData, setSkuData] = useState<SkuProps>({
    sku: "",
  });
  const [selectedSku, setSelectedSku] = useState("");
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
  }, [allCoinsDataLoading, allCoinsData]);

  if (allCoinsDataLoading) return <h1>Loading</h1>;

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setSkuData({ ...skuData, [name]: value });
  };

  return (
    <div className="grid grid-cols-12">
      <form className="col-span-10">
        <FormFields
          htmlFor="sku"
          type="text"
          name="sku"
          placeholder="SKU"
          value={skuData.sku}
          onChange={handleFormChange}
        />
        <HiOutlineShoppingCart
          className="text-4xl hover:cursor-pointer justify-self-center hover:text-green-500 rounded"
          onClick={() => dispatch(addToCart(skuData))}
        />
      </form>

      {/* <div>
        <button onClick={openSearchCoins}>Open Modal</button>
        <SearchCoinsModal
          isOpen={isSearchCoinsOpen}
          onClose={closeSearchCoins}
        />
      </div> */}
    </div>
  );
};

export default SalesInvoice;
