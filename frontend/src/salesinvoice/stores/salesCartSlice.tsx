import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SalesCartSlice {
  items: object[];
}

const initialState: SalesCartSlice = {
  items: [],
};

export const salesCartSlice = createSlice({
  name: "salesCart",
  initialState,
  reducers: {
    addToCart: (state: SalesCartSlice, action: PayloadAction<object>) => {
      state.items.push(action.payload);
    },
    itemsInCart: (state: SalesCartSlice) => {
      state.items;
    },
  },
});

export const { addToCart, itemsInCart } = salesCartSlice.actions;

export default salesCartSlice.reducer;
