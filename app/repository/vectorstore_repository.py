import os
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_vectorstore():
    if os.path.exists("app/resources/chroma_db_all_products/"):
        print("Loading existing ChromaDB...")
        vectors = Chroma(
            persist_directory="app/resources/chroma_db_all_products/",
            embedding_function=OpenAIEmbeddings()
        )
    else:
        print("Creating ChromaDB...")
        embeddings = OpenAIEmbeddings()
        loader = PyPDFDirectoryLoader("app/resources/data-produk-asuransi-brins")
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        final_documents = text_splitter.split_documents(docs[:50])
        vectors = Chroma.from_documents(
            documents=final_documents,
            embedding=embeddings,
            persist_directory="app/resources/chroma_db_all_products/"
        )
        vectors.persist()
    return vectors
