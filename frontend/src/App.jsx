import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

function App() {
  const [data, setData] = useState([])
  useEffect(()=> {
    async function fetchData(){
      console.log(import.meta.env.VITE_API_URL)
      try{
        const response = await fetch(`${import.meta.env.VITE_API_URL}post`);
        if (!response.ok){
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        console.log(result)
        setData(result);
      } catch (error) {
        console.error('Error fetching data',error);
      }
    }
    fetchData();
  }, [])

  return (
    <>
      hello world
    </>
  )
}

export default App
