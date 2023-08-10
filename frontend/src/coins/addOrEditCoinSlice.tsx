import { createSlice } from "@reduxjs/toolkit";
// import type { PayloadAction } from "@reduxjs/toolkit";

export interface AddOrEditCoinState {
  isEdit: boolean;
}

const initialState: AddOrEditCoinState = {
  isEdit: false,
};

export const addOrEditCoinSlice = createSlice({
  name: "addOrEditCoin",
  initialState,
  reducers: {
    changeBoolean: (state: AddOrEditCoinState) => {
      state.isEdit = !state.isEdit;
    },
  },
});

export const { changeBoolean } = addOrEditCoinSlice.actions;

export default addOrEditCoinSlice.reducer;
