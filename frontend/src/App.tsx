import { useState, useEffect } from 'react'
import './App.css'

interface FormProps {
  onSubmit: (data: FormData) => void;
}
interface FormData {
  pcgs_number?: null;
  title: string;
  year: null;
  year2?: null;
  description?: string;
  cost: null;
  quantity: number;
  sale_price: null;
  mint: string,
  family_of_coin: string,
  denomination_of_coin: string,
  coin_type: number,
  grading: number,
  grade: number | string,
  grade2?: number | string,
  images?: File,
}

// function Form({ onSubmit }: FormProps ) {
//   const [formData, setFormData] = useState<FormData>({
//     pcgs_number: null,
//     title: '',
//     year: null,
//     year2: null,
//     description: '',
//     cost: null,
//     quantity: 1,
//     sale_price: null,
//     mint: 'P',
//     family_of_coin: '',

//   });

// }


function App() {
  const coinUrl = 'http://localhost:8000/api/coins/'

  return (
    <>
      <h1>Vitdftgedrfgdfgsafdsafe</h1>
      <div className="card">
        
        <p>
          Edit <code>src/App.tsx </code>${coinUrl}
        </p>
        <input type='number' name='pcgs_number' id='pcgs_number'></input>
      </div>
      
    </>
  )
}

export default App
