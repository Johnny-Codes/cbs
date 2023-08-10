import { useState } from "react";
import CoinMenu from "./CoinMenu";
import CoinList from "./CoinList";
import AddCoinForm from "./AddCoinForm";
import { useSelector, useDispatch } from "react-redux";
import { changeBoolean } from "./addOrEditCoinSlice";
import { RootState } from "../store";

export default function CoinMenuAndList() {
  const [selectedCoinType, setSelectedCoinType] = useState();
  const isEdit = useSelector((state: RootState) => state.changeBoolean.isEdit);
  const baseUrl = "http://localhost:8000";

  const handleSelectedCoinType = (e) => {
    setSelectedCoinType(e.target.getAttribute("data-url"));
  };

  let fetchUrl;
  if (!selectedCoinType) {
    fetchUrl = null;
  } else {
    fetchUrl = `${baseUrl}${selectedCoinType}`;
  }

  return (
    <div className="grid grid-cols-12">
      <div className="col-span-2">
        <CoinMenu selectedCoin={handleSelectedCoinType} />
      </div>

      <div className="col-span-10">
        {!isEdit ? <CoinList url={fetchUrl} /> : <AddCoinForm />}
      </div>
    </div>
  );
}
