import React, {useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect (() => {
    fetch("http://127.0.0.1:5000/all-news").then(
      (res) => {
        return res.json();
      }
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>

    </div>
  )
}

export default App