import GetCoinFamily from "./GetCoinFamily";
import { useState, useEffect } from "react";
import AddCoinForm from "./AddCoinForm";

const CoinTypeComponent = ({ coinType, selectedCoin }) => {
  return (
    <div className="hs-accordion-group">
      {coinType.map((coin) => (
        <div className="hs-accordion-content" key={coin.id}>
          {/* <a href={`http://localhost:8000${coin.url}`}> */}

          <p
            data-url={coin.url}
            onClick={selectedCoin}
            className="p-2 border-b-2 border-x-2 border-black  text-gray-800 dark:text-gray-200"
          >
            {coin.coin_type}
          </p>
          {/* </a> */}
        </div>
      ))}
    </div>
  );
};

const DenominationComponent = ({
  denominations,
  openAccordions,
  toggleAccordion,
  selectedCoin,
}) => {
  return (
    <div className="hs-accordion-group">
      {denominations.map((d) => (
        <div
          className="hs-accordion"
          id={`hs-basic-nested-sub-heading-${d.id}`}
          key={d.id}
        >
          <button
            className="border-2 border-black bg-sky-300 hs-accordion-toggle hs-accordion-active:text-blue-600 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-left text-gray-800 transition hover:text-gray-500 dark:hs-accordion-active:text-blue-500 dark:text-gray-200 dark:hover:text-gray-400"
            onClick={() =>
              toggleAccordion(`hs-basic-nested-sub-collapse-${d.id}`)
            }
            aria-controls={`hs-basic-nested-sub-collapse-${d.id}`}
            aria-expanded={openAccordions.includes(
              `hs-basic-nested-sub-collapse-${d.id}`
            )}
          >
            - {d.denomination_of_coin}
          </button>
          <div
            id={`hs-basic-nested-sub-collapse-${d.id}`}
            className={`hs-accordion-content ${
              openAccordions.includes(`hs-basic-nested-sub-collapse-${d.id}`)
                ? "block"
                : "hidden"
            } w-full overflow-hidden transition-[height] duration-300`}
            aria-labelledby={`hs-basic-nested-sub-heading-${d.id}`}
          >
            <CoinTypeComponent
              coinType={d.coin_type_name}
              openAccordions={openAccordions}
              toggleAccordion={toggleAccordion}
              selectedCoin={selectedCoin}
            />
          </div>
        </div>
      ))}
    </div>
  );
};

const FamilyComponent = ({
  family,
  openAccordions,
  toggleAccordion,
  selectedCoin,
}) => {
  return (
    <div className="hs-accordion-group">
      {family.map((fam) => (
        <div
          className="hs-accordion"
          id={`hs-basic-nested-heading-${fam.id}`}
          key={fam.id}
        >
          <button
            className="border-2 border-black bg-sky-400 hs-accordion-toggle hs-accordion-active:text-blue-600 py-3 inline-flex items-center gap-x-3 w-full font-semibold text-left text-gray-800 transition hover:text-gray-500 dark:hs-accordion-active:text-blue-500 dark:text-gray-200 dark:hover:text-gray-400"
            onClick={() =>
              toggleAccordion(`hs-basic-nested-collapse-${fam.id}`)
            }
            aria-controls={`hs-basic-nested-collapse-${fam.id}`}
            aria-expanded={openAccordions.includes(
              `hs-basic-nested-collapse-${fam.id}`
            )}
          >
            {fam.type}
          </button>
          <div
            id={`hs-basic-nested-collapse-${fam.id}`}
            className={`hs-accordion-content ${
              openAccordions.includes(`hs-basic-nested-collapse-${fam.id}`)
                ? "block"
                : "hidden"
            } w-full overflow-hidden transition-[height] duration-300`}
            aria-labelledby={`hs-basic-nested-heading-${fam.id}`}
          >
            <DenominationComponent
              denominations={fam.denominations}
              openAccordions={openAccordions}
              toggleAccordion={toggleAccordion}
              selectedCoin={selectedCoin}
            />
          </div>
        </div>
      ))}
    </div>
  );
};

export default function CoinMenu({ selectedCoin }) {
  const [family, setFamily] = useState([]);
  const [openAccordions, setOpenAccordions] = useState([]);

  useEffect(() => {
    GetCoinFamily(setFamily);
  }, []);

  const toggleAccordion = (accordionId) => {
    setOpenAccordions((prevState) =>
      prevState.includes(accordionId)
        ? prevState.filter((id) => id !== accordionId)
        : [...prevState, accordionId]
    );
  };

  return (
    <div>
      <FamilyComponent
        family={family}
        openAccordions={openAccordions}
        toggleAccordion={toggleAccordion}
        selectedCoin={selectedCoin}
      />
    </div>
  );
}
