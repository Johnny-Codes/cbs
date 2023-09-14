import {
  FetchArgs,
  createApi,
  fetchBaseQuery,
} from "@reduxjs/toolkit/query/react";

export const invoicesApi = createApi({
  reducerPath: "invoiceApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  tagTypes: ["Invoice"],
  endpoints: (builder) => ({
    submitSalesCart: builder.mutation({
      query: (data) => (
        console.log("data", data),
        {
          url: "sales/invoice/",
          method: "POST",
          body: data,
        }
      ),
    }),
  }),
});

export const { useSubmitSalesCartMutation } = invoicesApi;
