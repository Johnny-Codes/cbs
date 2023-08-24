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
    setEditMode: (state: AddOrEditCoinState) => {
      state.isEdit = true;
    },
    setAddMode: (state: AddOrEditCoinState) => {
      state.isEdit = false;
    },
  },
});

export const { setEditMode, setAddMode } = addOrEditCoinSlice.actions;

export default addOrEditCoinSlice.reducer;
