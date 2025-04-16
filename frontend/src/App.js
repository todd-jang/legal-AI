
import React from "react";

function App() {
  const [response, setResponse] = React.useState("");

  const fetchAnswer = async () => {
    const res = await fetch("http://localhost:8000/query?q=법률 AI는 뭐야?");
    const data = await res.json();
    setResponse(data.answer);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🧠 Legal AI Assistant</h1>
      <button onClick={fetchAnswer}>법률 질문 보내기</button>
      <p>응답: {response}</p>
    </div>
  );
}

export default App;
