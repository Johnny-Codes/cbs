const getCoinFamily = async (
  setFamily: React.Dispatch<React.SetStateAction<never[]>>
) => {
  try {
    const response = await fetch("http://localhost:8000/api/coins/family/");
    if (response.ok) {
      const json = await response.json();
      setFamily(json);
    }
  } catch (error) {
    console.log("error", error);
  }
};

export default getCoinFamily;
