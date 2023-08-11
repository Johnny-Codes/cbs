const getCoinGradingServices = async (
  setCoinGradingServices: React.Dispatch<React.SetStateAction<never[]>>
) => {
  try {
    const response = await fetch(
      "http://localhost:8000/api/coins/gradingservices/"
    );
    if (response.ok) {
      const json = await response.json();
      setCoinGradingServices(json);
    }
  } catch (error) {
    console.log("error", error);
  }
};

export default getCoinGradingServices;
