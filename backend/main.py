
from fastapi import FastAPI, Query
from retriever import get_answer

app = FastAPI()

@app.get("/query")
def query(q: str = Query(...)):
    answer = get_answer(q)
    return {"answer": answer}
