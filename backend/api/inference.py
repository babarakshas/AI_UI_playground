from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.dummy_model import predict

router = APIRouter()


class InferenceRequest(BaseModel):
    text: str


class InferenceResponse(BaseModel):
    input: str
    output: str
    confidence: float


@router.post("/predict", response_model=InferenceResponse)
def run_inference(request: InferenceRequest):
    result = predict(request.text)
    return resultfrom fastapi import APIRouter
from pydantic import BaseModel
from backend.models.dummy_model import predict

router = APIRouter()


class InferenceRequest(BaseModel):
    text: str


class InferenceResponse(BaseModel):
    input: str
    output: str
    confidence: float


@router.post("/predict", response_model=InferenceResponse)
def run_inference(request: InferenceRequest):
    result = predict(request.text)
    return result

