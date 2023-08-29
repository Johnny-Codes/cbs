import { useState, useEffect } from "react";
import CoinMenu from "./CoinMenu";
import CoinList from "./CoinList";
import AddCoinForm from "./AddCoinForm";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../store";

export default function CoinMenuAndList() {
  const [selectedCoinType, setSelectedCoinType] = useState();
  const isEdit = useSelector((state: RootState) => state.changeBoolean.isEdit);
  const baseUrl = "http://localhost:8000";

  const handleSelectedCoinType = (e) => {
    setSelectedCoinType(e.target.getAttribute("data-url"));
  };

  const [fetchUrl, setFetchUrl] = useState("");
  useEffect(() => {
    setFetchUrl(`${baseUrl}${selectedCoinType}`);
  }, [selectedCoinType]);

  return (
    <div className="grid grid-cols-12">
      <div className="col-span-2">
        <CoinMenu selectedCoin={handleSelectedCoinType} />
      </div>

      <div className="col-span-10">
        {!isEdit ? <CoinList url={fetchUrl} /> : <AddCoinForm />}
        {/* <AddCoinForm /> */}
      </div>
    </div>
  );
}
