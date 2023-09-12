import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";

import { coinApi } from "./coins/services/coins";
import { customersApi } from "./customers/services/customers";

import addOrEditCoinSlice from "./coins/addOrEditCoinSlice";
import selectedCoinSlice from "./coins/selectedCoinSlice";

import customerSlice from "./customers/customerSlice";

import salesCartSlice from "./salesinvoice/salesCartSlice";

export const store = configureStore({
  reducer: {
    changeBoolean: addOrEditCoinSlice,
    selectedCoinId: selectedCoinSlice,
    selectedCustomerId: customerSlice,
    addToCart: salesCartSlice,
    itemsInCart: salesCartSlice,
    [coinApi.reducerPath]: coinApi.reducer,
    [customersApi.reducerPath]: customersApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(coinApi.middleware, customersApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;

setupListeners(store.dispatch);
