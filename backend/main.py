from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.inference import router as inference_router

app = FastAPI(title="AI UI Playground")

# Allow frontend JS to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inference_router)


@app.get("/")
def health():
    return {"status": "ok"}# backend/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "ok"}
