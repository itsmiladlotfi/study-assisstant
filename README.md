## Objective 🎯

This project utilizes Langchain and Gorq to establish a simple Retrieval system. This system empowers you to ask questions about your notes(animal biology for example), it works by first performing a retrieval step when presented with a question. This step fetches relevant text from faiss vector database, where the documents have been indexed.

## Quickstart

### Setup Python environment



```bash
python -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


### Setup .env file with API tokens needed.

```
GORQ_API_KEY="<Put your token here>"

```

### Start Uvicorn

```
uvicorn main:app --reload        

```

## Example Query for api call

```

curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question": "جانداران چند گونه هستند؟"}'
```
