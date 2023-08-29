import { useSoftDeleteCoinMutation } from "./services/coins";

const HandleDelete = (id: number) => {
  const [deleteCoin, response] = useSoftDeleteCoinMutation();
  deleteCoin(id);
};

export default HandleDelete;
