import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";

import { coinApi } from "./coins/services/coins";

import addOrEditCoinSlice from "./coins/addOrEditCoinSlice";
import selectedCoinSlice from "./coins/selectedCoinSlice";

export const store = configureStore({
  reducer: {
    changeBoolean: addOrEditCoinSlice,
    selectedCoinId: selectedCoinSlice,
    [coinApi.reducerPath]: coinApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(coinApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;

setupListeners(store.dispatch);
