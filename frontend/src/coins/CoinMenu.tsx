import GetCoinFamily from "./GetCoinFamily";
import { useState, useEffect } from "react";

const CoinTypeComponent = ({ coinType }) => {
  return (
    <ul>
      {coinType.map((coin) => (
        <li key={coin.id} id={coin.id}>
          {/* this actually needs to be a <Link> to a component */}
          {/* <a href={`http://localhost:8000${coin.url}`}> */}
          {/* something like: <listCoinTypes url={coin.url} */}
          {/* how to do cache? big db might need it. React query? */}
          {coin.coin_type}
          {/* </a> */}
        </li>
      ))}
    </ul>
  );
};

const DenominationComponent = ({ denominations }) => {
  return (
    <ul>
      {denominations.map((d) => (
        <>
          <li key={d.id} id={d.id}>
            {d.denomination_of_coin}
          </li>
          <CoinTypeComponent coinType={d.coin_type_name} />
        </>
      ))}
    </ul>
  );
};

const FamilyComponent = ({ family }) => {
  return (
    <ul>
      {family.map((fam) => (
        <>
          <li key={fam.id} className="text-3xl font-bold underline">
            {fam.type}
          </li>
          <DenominationComponent denominations={fam.denominations} />
        </>
      ))}
    </ul>
  );
};

export default function CoinMenu() {
  const [family, setFamily] = useState([]);

  useEffect(() => {
    GetCoinFamily(setFamily);
  }, []);

  return <FamilyComponent family={family} />;
}
