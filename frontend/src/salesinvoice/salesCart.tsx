import { RootState } from "../store";
import { useSelector, useDispatch } from "react-redux";
import { useSubmitSalesCartMutation } from "./api/invoicesApi";
import { removeFromCart } from "./stores/salesCartSlice";
import { AiFillDelete } from "react-icons/ai";
import { useEffect } from "react";
const SalesCart = () => {
  const itemsInTheCart = useSelector(
    (state: RootState) => state.itemsInCart.skus
  );
  console.log("items in cart", itemsInTheCart);
  const dispatch = useDispatch();
  const [submitCart, submitCartResponse] = useSubmitSalesCartMutation();
  const handleSubmitSalesCart = () => {
    console.log("submitting sales cart");
    submitCart(itemsInTheCart);
  };

  useEffect(() => {
    if (submitCartResponse.isSuccess) {
      console.log("component success");
    }
    if (submitCartResponse.isError) {
      console.log("component error");
    }
  }, [submitCartResponse]);

  return (
    <>
      <div>
        {itemsInTheCart?.map((item, index) => (
          <div
            key={index}
            className="grid grid-cols-2 py-2 even:bg-gray-200 odd:bg-gray-400"
          >
            <span className="pl-2">{item.sku}</span>
            <AiFillDelete
              onClick={() => dispatch(removeFromCart(index))}
              className="justify-self-center hover:cursor-pointer hover:text-red-500"
            />
          </div>
        ))}
      </div>
      <button onClick={handleSubmitSalesCart}>Checkout</button>
    </>
  );
};

export default SalesCart;
