from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(
        ...,
        json_schema_extra={"example": "Explain cloud computing"}
    )

class ExplanationResponse(BaseModel):
    response: str
    source: str

class ErrorResponse(BaseModel):
    detail: str
