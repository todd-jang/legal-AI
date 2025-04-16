
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def get_answer(query: str) -> str:
    db = Chroma(persist_directory="chroma_db", embedding_function=OpenAIEmbeddings())
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
    return qa.run(query)
