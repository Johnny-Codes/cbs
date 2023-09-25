import { useState, useEffect } from "react";
import { useCustomerSalesHistoryQuery } from "./api/invoicesApi";
import { useGetCustomerDetailQuery } from "../customers/api/customers";
import { useSelector } from "react-redux";
import { RootState } from "../store";
import formatDate from "../helpers/formatDate";
import grandTotal from "../helpers/grandTotal";
import { useParams } from "react-router-dom";

const CustomerSalesHistory = () => {
  const { customerId } = useParams();
  const {
    data: customerSalesHistoryData,
    isLoading: customerSalesHistoryDataLoading,
  } = useCustomerSalesHistoryQuery(customerId);
  const { data: customerDetail, isLoading: customerDetailLoading } =
    useGetCustomerDetailQuery(customerId);
  const [customerSalesHistory, setCustomerSalesHistory] = useState([]);
  const [customerDetailData, setCustomerDetailData] = useState({});
  useEffect(() => {
    setCustomerSalesHistory(customerSalesHistoryData);
    setCustomerDetailData(customerDetail);
  }, [customerSalesHistoryData, customerDetail]);

  if (customerSalesHistoryDataLoading) return <h1>Loading...</h1>;
  if (customerDetailLoading) return <h1>Loading...</h1>;

  console.log("saleshistorydata", customerSalesHistoryData);
  console.log("length", customerSalesHistoryData[0]?.sales_item?.length);
  console.log("customer detail", customerDetailData);

  return (
    <>
      <div>
        {customerDetailData.first_name} {customerDetailData.last_name}
      </div>
      <div>
        <table className="table-auto">
          <thead>
            <tr className="bg-blue-500 text-white">
              <th>Invoice</th>
              <th>Date</th>
              <th>Number of Items</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            {customerSalesHistory && customerSalesHistory.length > 0 ? (
              customerSalesHistory.map((record: {}) => (
                <tr
                  key={record.id}
                  className="even:bg-slate-200 odd:bg-slate-400"
                >
                  <td>{record.id}</td>
                  <td>{formatDate(record.invoice_date)}</td>
                  <td>{record.sales_item.length}</td>
                  <td>$ {grandTotal(record.sales_item)}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4">No History</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </>
  );
};

export default CustomerSalesHistory;
