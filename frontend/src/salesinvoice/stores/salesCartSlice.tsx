import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SalesCartSlice {
  skus: object[];
  customer: number;
}

const initialState: SalesCartSlice = {
  skus: [],
  customer: 0,
};

export const salesCartSlice = createSlice({
  name: "salesCart",
  initialState,
  reducers: {
    addToCart: (state: SalesCartSlice, action: PayloadAction<object>) => {
      state.skus.push(action.payload);
    },
    itemsInCart: (state: SalesCartSlice) => {
      state.skus;
    },
    removeFromCart: (state: SalesCartSlice, action: PayloadAction<number>) => {
      state.skus.splice(action.payload, 1);
    },
    addCustomerId: (state: SalesCartSlice, action: PayloadAction<number>) => {
      state.customer = action.payload;
    },
  },
});

export const { addToCart, itemsInCart, removeFromCart, addCustomerId } =
  salesCartSlice.actions;

export default salesCartSlice.reducer;
