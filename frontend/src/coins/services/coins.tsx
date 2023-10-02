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
      providesTags: ["Coins"],
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
        console.log("submited id", id);
        let url = `http://localhost:8000/api/coins/`;
        if (id) {
          url = `coins/${id}/`;
        }
        console.log("submit url", url);
        console.log("data submitted", data);

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
