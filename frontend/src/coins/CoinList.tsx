import { useState, useEffect } from "react";

type CoinListType = {
  url: string;
};

export default function CoinList({ url }: CoinListType) {
  const [coin, setCoin] = useState([]);

  console.log("url prop", url);
  const fetchData = async () => {
    try {
      const response = await fetch(url);
      if (response.ok) {
        const json = await response.json();
        setCoin(json);
      }
    } catch (error) {
      console.log("error", error);
    }
  };
  useEffect(() => {
    fetchData();
  }, url);

  if (!url) {
    return <h1>Please select a coin</h1>;
  }

  return (
    <div>
      <table className="table-auto border-collapse w-full">
        <thead>
          <tr className="bg-blue-500">
            <th className="border border-black p-2">SKU</th>
            <th className="border border-black p-2">Title</th>
            <th className="border border-black p-2">Quantity</th>
            <th className="border border-black p-2">Cost</th>
            <th className="border border-black p-2">Total Cost</th>
            <th className="border border-black p-2">Edit</th>
          </tr>
        </thead>
        <tbody>
          {coin &&
            coin.map((c) => (
              <tr key={c.id} className="even:bg-blue-200 odd:bg-white">
                <td className="border border-black p-2">{c.sku}</td>
                <td className="border border-black p-2">{c.title}</td>
                <td className="border border-black p-2">{c.cost}</td>
                <td className="border border-black p-2">{c.quantity}</td>
                <td className="border border-black p-2">
                  {c.cost * c.quantity}
                </td>
                <td className="border border-black p-2">edit button(s) here</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}
