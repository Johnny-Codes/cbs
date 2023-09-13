import { RootState } from "../store";
import { useSelector } from "react-redux/es/hooks/useSelector";

const SalesCart = () => {
  const itemsInTheCart = useSelector(
    (state: RootState) => state.itemsInCart.items
  );
  console.log("items in cart", itemsInTheCart);
  return (
    <div>
      {itemsInTheCart?.map((item, index) => (
        <div key={index}>
          {item.sku} - {item.quantity}
        </div>
      ))}
    </div>
  );
};

export default SalesCart;
