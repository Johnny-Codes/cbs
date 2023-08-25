import {
  FetchArgs,
  createApi,
  fetchBaseQuery,
} from "@reduxjs/toolkit/query/react";

export const customersApi = createApi({
  reducerPath: "customersApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  tagTypes: ["Customers"],
  endpoints: (builder) => ({
    getAllCustomers: builder.query({
      query: () => "customers/",
      providesTags: ["Customers"],
    }),
    addCustomer: builder.mutation({
      query: ({ data, id, method }) => {
        let url = `customers/`;
        if (id !== "") {
          url = `customers/${id}/`;
        }

        return {
          url: url,
          method: method,
          body: data,
        };
      },
      invalidatesTags: ["Customers"],
    }),
    getCustomerDetail: builder.query({
      query: (customerId: number): string | FetchArgs => {
        if (customerId !== null) {
          const url = `customers/${customerId}/`;
          return url;
        }
        return "";
      },
    }),
  }),
});

export const {
  useGetAllCustomersQuery,
  useAddCustomerMutation,
  useGetCustomerDetailQuery,
} = customersApi;
