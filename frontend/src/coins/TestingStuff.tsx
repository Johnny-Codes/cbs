import { useGetAllCoinsQuery } from "./services/coins";

const TestingStuff = () => {
  const { data, error, isLoading } = useGetAllCoinsQuery("");

  return (
    <div>
      {error ? (
        <>
          <h1>error</h1>
        </>
      ) : isLoading ? (
        <>
          <h1>loading</h1>
        </>
      ) : data ? (
        <>
          {data.map((x) => (
            <p key={`${x.id}`}>{x.title}</p>
          ))}
        </>
      ) : null}
    </div>
  );
};

export default TestingStuff;
