const getCoinGrades = async (
  setCoinGrades: React.Dispatch<React.SetStateAction<never[]>>
) => {
  try {
    const response = await fetch("http://localhost:8000/api/coins/coingrades/");
    if (response.ok) {
      const json = await response.json();
      setCoinGrades(json);
    }
  } catch (error) {
    console.log("error", error);
  }
};

export default getCoinGrades;
