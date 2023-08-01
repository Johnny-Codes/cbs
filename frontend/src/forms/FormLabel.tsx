type TextType = {
    text: string
    htmlFor: string
}

const FormLabel = ({text, ...rest}:TextType) => {
    return <label {...rest}>{text}</label>
}

export default FormLabel