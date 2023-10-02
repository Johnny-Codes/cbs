import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import FormTextarea from "../forms/FormTextarea";
import SubmitButton from "../buttons/SubmitButton";
import { addNotesToCart } from "./stores/salesCartSlice";
import { RootState } from "../store";
import { itemsInCart } from "./stores/salesCartSlice";

const SalesNotes = () => {
  const itemsInTheCart = useSelector((state: RootState) => state.itemsInCart);
  const [notes, setNotes] = useState<string>("");
  const dispatch = useDispatch();

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    dispatch(addNotesToCart(notes));
    console.log(itemsInTheCart);
    setNotes("");
  };

  console.log(notes);

  return (
    <>
      <h3>Sales Notes</h3>
      <form onSubmit={handleSubmit}>
        <FormTextarea onChange={(e) => setNotes(e.target.value)} />
        <SubmitButton />
      </form>
    </>
  );
};

export default SalesNotes;
