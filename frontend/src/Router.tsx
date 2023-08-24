import { BrowserRouter, Routes, Route, useHistory } from "react-router-dom";
import CoinMenuAndList from "./coins/CoinMenuAndList";
import AddCoinForm from "./coins/AddCoinForm";
import NavBar from "./nav/NavBar";

function Router() {
  return (
    <BrowserRouter>
      <NavBar />

      <Routes>
        <Route path="/inventory" element={<CoinMenuAndList />} />
        <Route path="/add-coin" element={<AddCoinForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
