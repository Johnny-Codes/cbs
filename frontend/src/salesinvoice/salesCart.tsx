import { RootState } from "../store";
import { useSelector, useDispatch } from "react-redux";
import { useSubmitSalesCartMutation } from "./api/invoicesApi";
import { removeFromCart } from "./stores/salesCartSlice";
import { AiFillDelete } from "react-icons/ai";
import { useEffect } from "react";
import { useGetCustomerDetailQuery } from "../customers/api/customers";
const SalesCart = () => {
  const itemsInTheCart = useSelector((state: RootState) => state.itemsInCart);

  const dispatch = useDispatch();
  const [submitCart, submitCartResponse] = useSubmitSalesCartMutation();
  const handleSubmitSalesCart = () => {
    submitCart(itemsInTheCart);
  };
  const { data: customerData, isLoading: customerDataLoading } =
    useGetCustomerDetailQuery(itemsInTheCart.customer);

  useEffect(() => {
    if (submitCartResponse.isSuccess) {
      console.log("component success");
    }
    if (submitCartResponse.isError) {
      console.log("component error");
    }
  }, [submitCartResponse]);
  if (customerDataLoading) return <h1>Loading...</h1>;
  return (
    <>
      <div>
        <div>
          Customer: {customerData?.first_name} {customerData?.last_name}
        </div>
        <div className="grid grid-cols-12 py-2">
          <div className="col-span-6">SKU</div>
          <div className="col-span-2">QTY</div>
          <div className="col-span-2">Price</div>
          <div className="col-span-2">Remove</div>
        </div>
        {itemsInTheCart?.skus.map((item, index) => (
          <div
            key={index}
            className="grid grid-cols-12 py-2 even:bg-gray-200 odd:bg-gray-400"
          >
            <div className="pl-2 col-span-6">{item.sku}</div>
            <div className="pl-2 col-span-2">{item.quantity}</div>
            <div className="pl-2 col-span-2">{item.price}</div>
            <div>
              <AiFillDelete
                onClick={() => dispatch(removeFromCart(index))}
                className="col-span-2 text-2xl justify-self-center hover:cursor-pointer hover:text-red-500"
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
