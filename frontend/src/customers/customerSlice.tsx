import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface CustomerState {
  id: number | null;
}

const initialState: CustomerState = {
  id: 1,
};

export const customerSlice = createSlice({
  name: "selectedCustomer",
  initialState,
  reducers: {
    selectedCustomerId: (
      state: CustomerState,
      action: PayloadAction<number | null>
    ) => {
      state.id = action.payload;
    },
  },
});

export const { selectedCustomerId } = customerSlice.actions;

export default customerSlice.reducer;
