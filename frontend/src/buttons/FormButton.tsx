import "./submitbutton.css";

export default function FormButton({text, ...rest}) {
  return <button {...rest}>{text}</button>;
}
