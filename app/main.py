from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {'status': 'ok'}

class EchoRequest(BaseModel):
    message: str

@app.post("/echo")
def echo(body: EchoRequest):
    return {'message': body.message}

