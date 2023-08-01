type FormSelectProps = {
  name: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  selectText: string;
  mapData: [];
};

const FormSelect = ({
  name,
  onChange,
  selectText,
  mapData,
}: FormSelectProps) => {
  return (
    <div>
      <select name={name} onChange={onChange}>
        <option value="">{selectText}</option>
        {mapData.map((item) => (
          <option key={item.id} value={item.id}>
            {item.type}
          </option>
        ))}
      </select>
    </div>
  );
};

export default FormSelect;
