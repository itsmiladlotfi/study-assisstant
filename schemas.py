from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    content_type: str
    num_documents: int
    message: str

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str
    source_passage: str
