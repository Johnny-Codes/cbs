import { useState } from "react";
import AddCoinForm from "./coins/AddCoinForm";
import CoinMenu from "./coins/CoinMenu";
import CoinMenuAndList from "./coins/CoinMenuAndList";

const App: React.FC = () => {
  return (
    <>
      <CoinMenuAndList />
    </>
  );
};

export default App;
