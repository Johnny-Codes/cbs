import { useSoftDeleteCoinMutation } from "./services/coins";

const HandleDelete = (id: number) => {
  const [deleteCoin, response] = useSoftDeleteCoinMutation();
  console.log("modal id", id);
  console.log("deleteCoin", deleteCoin);
  deleteCoin(id);
  console.log("delete response", response);
};

export default HandleDelete;
