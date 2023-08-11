import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const coinApi = createApi({
  reducerPath: "coinApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  endpoints: (builder) => ({
    getAllCoins: builder.query({
      query: () => "coins/",
    }),
    getSpecificCoin: builder.query({
      query: (coinId) => `coins/${coinId}/`,
    }),
    getCoinFamily: builder.query({
      query: () => `coins/family/`,
    }),
  }),
});

export const {
  useGetAllCoinsQuery,
  useGetSpecificCoinQuery,
  useGetCoinFamilyQuery,
} = coinApi;
