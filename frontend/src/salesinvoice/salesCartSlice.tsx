import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SalesCartSlice {
  items: string[];
}

const initialState: SalesCartSlice = {
  items: [],
};

export const salesCartSlice = createSlice({
  name: "salesCart",
  initialState,
  reducers: {
    addToCart: (state: SalesCartSlice, action: PayloadAction<string>) => {
      state.items.push(action.payload);
      for (let item in state.items) {
        console.log("item", item);
      }
    },
    itemsInCart: (state: SalesCartSlice) => {
      state.items;
    },
  },
});

export const { addToCart, itemsInCart } = salesCartSlice.actions;

export default salesCartSlice.reducer;
