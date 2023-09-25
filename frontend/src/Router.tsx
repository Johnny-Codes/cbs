import { BrowserRouter, Routes, Route, useHistory } from "react-router-dom";
import CoinMenuAndList from "./coins/CoinMenuAndList";
import AddCoinForm from "./coins/AddCoinForm";
import NavBar from "./nav/NavBar";
import CustomersList from "./customers/CustomersList";
import AddOrEditCustomer from "./customers/AddOrEditCustomer";
import SalesInvoicePage from "./salesinvoice/SalesInvoicePage";
import CustomerSalesHistory from "./salesinvoice/CustomerSalesHistory";
function Router() {
  return (
    <BrowserRouter>
      <NavBar />

      <Routes>
        <Route path="/inventory" element={<CoinMenuAndList />} />
        <Route path="/add-coin" element={<AddCoinForm />} />
        <Route path="/customers/add" element={<AddOrEditCustomer />} />
        <Route path="/customers" element={<CustomersList />} />
        <Route
          path="/customers/:customerId/details"
          element={<CustomerSalesHistory />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
