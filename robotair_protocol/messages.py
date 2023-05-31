from pydantic import BaseModel
from typing import List


class Image(BaseModel):

    # required fields
    tag: str
    digest: str
    size: int  # bytes


class Service(BaseModel):

    # required fields
    state: str
    image: Image

    # optional fields
    ram_usage: int = 0  # bytes
    cpu_percentage: float = 0.0


class DeploymentStatusMessage(BaseModel):

    # required fields
    services: List[Service]


class ErrorMessage(BaseModel):

    # required fields
    reason: str
