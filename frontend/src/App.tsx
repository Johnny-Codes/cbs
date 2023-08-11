import CoinMenuAndList from "./coins/CoinMenuAndList";
import TestingStuff from "./coins/TestingStuff";
import AddCoinForm from "./coins/AddCoinForm";

const App: React.FC = () => {
  return (
    <>
      <CoinMenuAndList />
      <AddCoinForm />
    </>
  );
};

export default App;
