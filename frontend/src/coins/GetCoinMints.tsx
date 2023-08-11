const getCoinMints = async (
  setCoinMints: React.Dispatch<React.SetStateAction<never[]>>
) => {
  try {
    const response = await fetch("http://localhost:8000/api/coins/mints/");
    if (response.ok) {
      const json = await response.json();
      setCoinMints(json);
    }
  } catch (error) {
    console.log("error", error);
  }
};

export default getCoinMints;
