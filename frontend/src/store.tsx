import { configureStore } from "@reduxjs/toolkit";

import addOrEditCoinSlice from "./coins/addOrEditCoinSlice";
import selectedCoinSlice from "./coins/selectedCoinSlice";

export const store = configureStore({
  reducer: {
    changeBoolean: addOrEditCoinSlice,
    selectedCoinId: selectedCoinSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;
