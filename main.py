from fastapi import FastAPI, HTTPException
from schemas import GenerateRequest
from model import generate_chat

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Tên mô hình: Text Generation API using LFM2.5-350M:\n"
                   "Kiến trúc hệ thống: Client (Laptop) -> FastAPI -> HuggingFace Model -> JSON Response -> Swagger UI"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: GenerateRequest):
    if not req.messages:
        raise HTTPException(status_code=400, detail="Message is required")

    try:
        result = generate_chat([m.dict() for m in req.messages])

        return {
            "prompt": req.messages,
            "generated_text": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))