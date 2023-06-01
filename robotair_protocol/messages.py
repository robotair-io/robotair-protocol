from pydantic import BaseModel
from typing import List, Optional


class Image(BaseModel):

    # required fields
    tag: str
    digest: str
    size: int  # bytes


class Container(BaseModel):

    # required fields
    block_read: int  # bytes
    block_write: int  # bytes
    container: str
    container_id: str
    container_name: str
    cpu_percentage: float
    memory_percentage: float
    memory_used: int  # bytes
    memory_limit: int  # bytes
    net_download: int  # bytes
    net_upload: int  # bytes
    started_at: str


class Service(BaseModel):

    # required fields
    name: str  # NOTE: this is the service name according to the deployment!
    state: str
    image: Image

    # optional fields
    container: Optional[Container] = None


class DeploymentStatusMessage(BaseModel):

    # required fields
    robot: str
    services: List[Service]


class ErrorMessage(BaseModel):

    # required fields
    reason: str
