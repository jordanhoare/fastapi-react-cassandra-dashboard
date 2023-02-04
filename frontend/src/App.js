import React from "react";
import { useEffect } from "react";
import { useState } from "react";

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/api/v1/items").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )

  })
  return (
    <div>
      App
    </div>
  )
}

export default App