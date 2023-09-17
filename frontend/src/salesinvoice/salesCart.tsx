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
        <div className="grid grid-cols-12 py-2">
          <div className="col-span-3">SKU</div>
          <div className="col-span-3">Quantity</div>
          <div className="col-span-3">Price</div>
          <div className="col-span-3">Remove</div>
        </div>
        {itemsInTheCart?.map((item, index) => (
          <div
            key={index}
            className="grid grid-cols-12 py-2 even:bg-gray-200 odd:bg-gray-400"
          >
            <div className="pl-2 col-span-3">{item.sku}</div>
            <div className="pl-2 col-span-3">{item.quantity}</div>
            <div className="pl-2 col-span-3">{item.price}</div>
            <div>
              <AiFillDelete
                onClick={() => dispatch(removeFromCart(index))}
                className="col-span-3 text-2xl justify-self-center hover:cursor-pointer hover:text-red-500"
              />
            </div>
          </div>
        ))}
      </div>

      <button onClick={handleSubmitSalesCart}>Checkout</button>
    </>
  );
};

export default SalesCart;
