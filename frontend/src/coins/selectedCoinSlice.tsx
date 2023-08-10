import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface SelectedCoinState {
  id: number | null;
}

const initialState: SelectedCoinState = {
  id: null,
};

export const selectedCoinSlice = createSlice({
  name: "selectedCoin",
  initialState,
  reducers: {
    selectedCoinId: (
      state: SelectedCoinState,
      action: PayloadAction<number>
    ) => {
      state.id = action.payload;
    },
  },
});

export const { selectedCoinId } = selectedCoinSlice.actions;

export default selectedCoinSlice.reducer;
