const getCoinStrikes = async (
  setCoinStrikes: React.Dispatch<React.SetStateAction<never[]>>
) => {
  try {
    const response = await fetch("http://localhost:8000/api/coins/strike/");
    if (response.ok) {
      const json = await response.json();
      setCoinStrikes(json);
    }
  } catch (error) {
    console.log("error", error);
  }
};

export default getCoinStrikes;
