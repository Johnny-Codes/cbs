import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SalesCartSlice {
  skus: object[];
  customer: number;
  notes: string;
}

const initialState: SalesCartSlice = {
  skus: [],
  customer: 0,
  notes: "",
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
      state.customer;
      state.notes;
    },
    removeFromCart: (state: SalesCartSlice, action: PayloadAction<number>) => {
      state.skus.splice(action.payload, 1);
    },
    addCustomerId: (state: SalesCartSlice, action: PayloadAction<number>) => {
      state.customer = action.payload;
    },
    addNotesToCart: (state: SalesCartSlice, action: PayloadAction<string>) => {
      state.notes = action.payload;
    },
  },
});

export const {
  addToCart,
  itemsInCart,
  removeFromCart,
  addCustomerId,
  addNotesToCart,
} = salesCartSlice.actions;

export default salesCartSlice.reducer;
