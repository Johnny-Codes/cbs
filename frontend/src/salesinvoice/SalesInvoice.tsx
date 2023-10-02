import { useState, useEffect } from "react";
import {
  useGetAllActiveCoinsQuery,
  useGetAllCoinsQuery,
} from "../coins/services/coins";
import FormFields from "../forms/FormFields";
import { useDispatch } from "react-redux";
import { addToCart } from "./stores/salesCartSlice";
import { HiOutlineShoppingCart } from "react-icons/hi2";

type SkuProps = {
  sku: string;
  quantity: number;
  price: number;
};

const SalesInvoice = () => {
  const dispatch = useDispatch();
  const { data: allCoinsData, isLoading: allCoinsDataLoading } =
    useGetAllActiveCoinsQuery("false");
  const [allCoins, setAllCoins] = useState({});
  const [skuData, setSkuData] = useState<SkuProps>({
    sku: "",
    quantity: 0,
    price: 0,
  });
  const [filteredCoins, setFilteredCoins] = useState<string[]>([]);

  useEffect(() => {
    if (!allCoinsDataLoading) {
      setAllCoins(allCoinsData);
    }
  }, [allCoinsDataLoading, allCoinsData]);

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setSkuData({ ...skuData, [name]: value });
  };

  const handleSearchSkus = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = e.target;
    const filteredSKUs = allCoinsData.filter((coin) =>
      coin.sku.toLowerCase().includes(value.toLowerCase())
    );
    setFilteredCoins(filteredSKUs.map((coin) => coin.sku));
  };

  const handleAddToCart = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!skuData.sku || !skuData.quantity || !skuData.price) {
      console.log("skus missing");
    } else {
      dispatch(addToCart(skuData));
      setSkuData({ sku: "", quantity: 0, price: 0 });
    }
  };

  return (
    <div className="grid grid-cols-12">
      <div className="col-span-12">
        <FormFields
          htmlFor="sku"
          type="text"
          name="sku"
          placeholder="Search SKUs"
          value={skuData.sku}
          onChange={(e) => {
            handleFormChange(e);
            handleSearchSkus(e);
          }}
        />
      </div>
      <div className="col-span-12">
        <form>
          <select
            name="selectedSku"
            id="selectedSku"
            required
            value={skuData.sku}
            onChange={(e) => {
              const selectedSku = e.target.value;
              setSkuData({ ...skuData, sku: selectedSku });
            }}
          >
            <option value="">Select SKU</option>
            {filteredCoins.map((sku) => (
              <option key={sku} value={sku}>
                {sku}
              </option>
            ))}
          </select>
          <FormFields
            htmlFor="quantity"
            type="number"
            name="quantity"
            placeholder="Quantity"
            onChange={handleFormChange}
            required
            value={skuData.quantity}
          />
          <FormFields
            htmlFor="price"
            type="number"
            name="price"
            placeholder="Price"
            onChange={handleFormChange}
            required
            value={skuData.price}
          />
          <div className="col-span-12 justify-self-center">
            <HiOutlineShoppingCart
              className="text-4xl hover:cursor-pointer justify-self-center hover:text-green-500 rounded"
              onClick={(e) => handleAddToCart(e)}
            />
          </div>
        </form>
      </div>
    </div>
  );
};

export default SalesInvoice;
