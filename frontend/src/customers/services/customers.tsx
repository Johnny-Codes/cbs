import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const customersApi = createApi({
  reducerPath: "customersApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  endpoints: (builder) => ({
    getAllCustomers: builder.query({
      query: () => "customers/",
    }),
  }),
});

export const { useGetAllCustomersQuery } = customersApi;
