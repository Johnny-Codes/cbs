import { RootState } from "../store";
import { useSelector } from "react-redux/es/hooks/useSelector";
import { useSubmitSalesCartMutation } from "./api/invoicesApi";

const SalesCart = () => {
  const itemsInTheCart = useSelector(
    (state: RootState) => state.itemsInCart.items
  );
  console.log("items in cart", itemsInTheCart);
  const [submitCart, submitCartResponse] = useSubmitSalesCartMutation();
  const handleSubmitSalesCart = () => {
    console.log("submitting sales cart");
    submitCart(itemsInTheCart);
  };
  return (
    <>
      <div>
        {itemsInTheCart?.map((item, index) => (
          <div key={index}>
            {item.sku} - {item.quantity}
          </div>
        ))}
      </div>
      <button onClick={handleSubmitSalesCart}>Checkout</button>
    </>
  );
};

export default SalesCart;
