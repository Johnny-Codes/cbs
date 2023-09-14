import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SalesCartSlice {
  skus: object[];
}

const initialState: SalesCartSlice = {
  skus: [],
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
  },
});

export const { addToCart, itemsInCart, removeFromCart } =
  salesCartSlice.actions;

export default salesCartSlice.reducer;
