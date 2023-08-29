import React, { useEffect } from "react";
import { RootState } from "../store";
import { useSelector, useDispatch } from "react-redux";

const getCoinDetail = async (id: number | null, setFormData, formData) => {
  const coin = id;
  const baseUrl = "http://localhost:8000/api/coins/";
  if (id) {
    try {
      const response = await fetch(`${baseUrl}${coin}`);
      if (response.ok) {
        const json = await response.json();
        const updatedFormData = { ...formData, ...json };
        setFormData(updatedFormData);
        if (json.is_bulk) {
          const grade2 = document.getElementById("grade2");
          const year2 = document.getElementById("year2");
          grade2?.classList.toggle("hidden");
          year2?.classList.toggle("hidden");
        }
      }
    } catch (error) {
      console.log("error GetCoinDetail.tsx", error);
    }
  }
};

export default getCoinDetail;
