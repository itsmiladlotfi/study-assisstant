import os
import sys

from langchain_community.vectorstores import FAISS
from vector_db import load_and_process_document
from schemas import AnswerResponse, QuestionRequest
from fastapi import FastAPI, HTTPException
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
filepath = r"data\zist.pdf"
app = FastAPI()

vector_store = load_and_process_document(filepath=filepath)

llm = ChatGroq(model="mistral-saba-24b",
                temperature=0.3)

qa_chain = RetrievalQA.from_llm(
    llm=llm,
    retriever=vector_store,
    return_source_documents=True
)


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        result = qa_chain.invoke({"query": request.question})
        return {
            "question": request.question,
            "answer": result["result"],
            "source_passage": result["source_documents"][0].page_content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

