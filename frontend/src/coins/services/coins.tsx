import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const coinApi = createApi({
  reducerPath: "coinApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  tagTypes: ["Coins"],
  endpoints: (builder) => ({
    getAllActiveCoins: builder.query({
      query: (isDeleted) => `coins/?is_deleted=${isDeleted}`,
      providesTags: ["Coins"],
    }),
    getAllCoins: builder.query({
      query: () => `coins/`,
    }),
    getCoinTypeForCoinList: builder.query({
      query: (url) => `${url}?is_deleted=false`,
      providesTags: ["Coins"],
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
    softDeleteCoin: builder.mutation({
      query: (id) => ({
        url: `coins/${id}/`,
        method: "PUT",
        body: { toggle_soft_delete: true },
      }),
      invalidatesTags: ["Coins"],
    }),
    addCoinToInventory: builder.mutation({
      query: ({ data, id, method }) => {
        let url = `coins/`;
        if (id !== "") {
          url = `coins/${id}/`;
        }

        return {
          url: url,
          method: method,
          body: data,
        };
      },
      invalidatesTags: ["Coins"],
    }),
  }),
});

export const {
  useAddCoinToInventoryMutation,
  useGetAllCoinsQuery,
  useGetSpecificCoinQuery,
  useGetAllCoinFamiliesQuery,
  useGetAllCoinDenominationsQuery,
  useGetAllCoinTypeNamesQuery,
  useGetAllCoinGradesQuery,
  useGetAllCoinStrikesQuery,
  useGetAllCoinMintsQuery,
  useGetAllCoinGradingServicesQuery,
  useGetAllActiveCoinsQuery,
  useSoftDeleteCoinMutation,
  useGetCoinTypeForCoinListQuery,
} = coinApi;
