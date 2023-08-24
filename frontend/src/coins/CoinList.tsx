import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setEditMode } from "./addOrEditCoinSlice";
import { selectedCoinId } from "./selectedCoinSlice";
import EditButton from "../buttons/EditButton";
import { useGetAllActiveCoinsQuery } from "./services/coins";

export type CoinListType = {
  url: string;
};

export default function CoinList({ url }: CoinListType) {
  const dispatch = useDispatch();
  const { data: activeCoins } = useGetAllActiveCoinsQuery(false);

  console.log("active coins", activeCoins);
  useEffect(() => {
    activeCoins;
  }, [activeCoins]);
  const handleEdit = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    dispatch(setEditMode());
    dispatch(selectedCoinId(Number(e.target.value)));
  };

  // const handleDelete = (e: React.ChangeEvent<HTMLInputElement>) => {
  //   e.preventDefault();
  //   HandleDelete({ id: e.target.value });
  // };

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
          {activeCoins &&
            activeCoins.map((c) => (
              <tr
                key={c.id}
                value={c.id}
                className="even:bg-blue-200 odd:bg-white"
              >
                <td className="border border-black p-2">{c.sku}</td>
                <td className="border border-black p-2">{c.title}</td>
                <td className="border border-black p-2">{c.quantity}</td>
                <td className="border border-black p-2">{c.cost}</td>
                <td className="border border-black p-2">
                  {c.cost * c.quantity}
                </td>
                <td className="border border-black p-2">
                  <EditButton value={c.id} onClick={handleEdit} />
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}
