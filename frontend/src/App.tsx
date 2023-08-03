import AddCoinForm from "./coins/AddCoinForm";
import CoinMenu from "./coins/CoinMenu";

const App: React.FC = () => {
  return (
    <>
      <CoinMenu />
      <AddCoinForm />
    </>
  );
};

export default App;
