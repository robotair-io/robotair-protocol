from pydantic import BaseModel


class ErrorMessage(BaseModel):

    # required fields
    reason: str
