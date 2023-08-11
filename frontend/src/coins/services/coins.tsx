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
    getAllCoinFamilies: builder.query({
      query: () => `coins/family/`,
    }),
    getAllCoinDenominations: builder.query({
      query: () => `coins/denominations/`,
    }),
    getAllCoinTypeNames: builder.query({
      query: () => `coins/cointypes/`,
    }),
    getAllCoinGrades: builder.query({
      query: () => `coins/coingrades/`,
    }),
    getAllCoinStrikes: builder.query({
      query: () => `coins/strike/`,
    }),
    getAllCoinMints: builder.query({
      query: () => `coins/mints/`,
    }),
    getAllCoinGradingServices: builder.query({
      query: () => `coins/gradingservices/`,
    }),
  }),
});

export const {
  useGetAllCoinsQuery,
  useGetSpecificCoinQuery,
  useGetAllCoinFamiliesQuery,
  useGetAllCoinDenominationsQuery,
  useGetAllCoinTypeNamesQuery,
  useGetAllCoinGradesQuery,
  useGetAllCoinStrikesQuery,
  useGetAllCoinMintsQuery,
  useGetAllCoinGradingServicesQuery,
} = coinApi;
