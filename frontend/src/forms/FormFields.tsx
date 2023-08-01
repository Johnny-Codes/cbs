import FormInput from "./FormInput";
import FormLabel from "./FormLabel";
import FormTextarea from "./FormTextarea";

type FormFieldsProps = {
  labelText: string;
  htmlFor: string;
  type: "text" | "number" | "checkbox" | "textarea";
  value?: any;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  name: string;
};

const FormFields = ({
  labelText,
  htmlFor,
  type = "text",
  value,
  onChange,
  name,
  ...rest
}: FormFieldsProps) => {
  const isTextarea = type === "textarea";

  return (
    <div>
      <FormLabel text={labelText} htmlFor={htmlFor} />
      {isTextarea ? (
        <FormTextarea id={htmlFor} onChange={onChange} name={name} {...rest} />
      ) : (
        <FormInput
          type={type}
          id={htmlFor}
          value={value}
          onChange={onChange}
          name={name}
          {...rest}
        />
      )}
    </div>
  );
};

export default FormFields;
