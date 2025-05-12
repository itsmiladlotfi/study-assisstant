from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

embedding = HuggingFaceEmbeddings(model_name="heydariAI/persian-embeddings")


def load_and_process_document(filepath):

    loader = PyPDFLoader(filepath)
    documents = loader.load()
    

    text_splitter = CharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    splits = text_splitter.split_documents(documents)
    
    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embedding
    )
    
    return vectorstore.as_retriever()
    

