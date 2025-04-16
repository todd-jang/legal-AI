
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def vectorize_docs(folder_path="docs"):
    all_docs = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        loader = TextLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(all_docs)

    Chroma.from_documents(split_docs, OpenAIEmbeddings(), persist_directory="chroma_db").persist()

if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    with open("docs/sample.txt", "w") as f:
        f.write("법률 AI는 법적 정보를 분석하고 제공하는 인공지능입니다.")
    vectorize_docs()
