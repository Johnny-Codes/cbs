import CoinMenu from "./CoinMenu";
import CoinList from "./CoinList";
import { useState } from "react";

export default function CoinMenuAndList() {
  const [selectedCoin, setSelectedCoin] = useState();
  const baseUrl = "http://localhost:8000";
  const handleSelectedCoin = (e) => {
    console.log(
      "handle selected coin value",
      e.target.getAttribute("data-url")
    );
    setSelectedCoin(e.target.getAttribute("data-url"));
  };
  let fetchUrl;
  if (!selectedCoin) {
    fetchUrl = null;
  } else {
    fetchUrl = `${baseUrl}${selectedCoin}`;
  }

  return (
    <div className="grid grid-cols-12">
      <div className="col-span-2">
        <CoinMenu selectedCoin={handleSelectedCoin} />
      </div>
      <div className="col-span-10">
        <CoinList url={fetchUrl} />
      </div>
    </div>
  );
}
