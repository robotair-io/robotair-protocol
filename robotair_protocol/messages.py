from pydantic import BaseModel
from typing import List


class Image(BaseModel):

    # required fields
    tag: str
    digest: str
    size: int  # bytes


class Container(BaseModel):

    # required fields
    id: str

    # optional fields
    ram_usage: int = 0  # bytes
    cpu_percentage: float = 0.0


class Service(BaseModel):

    # required fields
    name: str  # NOTE: this is the service name relative to the deployment!
    state: str
    image: Image
    container: Container


class DeploymentStatusMessage(BaseModel):

    # required fields
    services: List[Service]


class ErrorMessage(BaseModel):

    # required fields
    reason: str
