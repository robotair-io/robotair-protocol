from pydantic import BaseModel
from typing import List, Optional


class Image(BaseModel):

    # required fields
    tag: str

    # optional fields
    digest: Optional[str] = None
    size: int = 0  # bytes


class Container(BaseModel):

    # required fields
    block_read: int  # bytes
    block_write: int  # bytes
    container: str
    container_id: str
    container_name: str
    cpu_percentage: float
    finished_at: str
    memory_percentage: float
    memory_used: int  # bytes
    memory_limit: int  # bytes
    net_download: int  # bytes
    net_upload: int  # bytes
    started_at: str
    status: str


class Service(BaseModel):

    # required fields
    name: str  # NOTE: this is the service name according to the deployment!
    image: Image

    # optional fields
    container: Optional[Container] = None


class DeploymentStatusMessage(BaseModel):

    # required fields
    identifier: str
    services: List[Service]


class SystemStatusMessage(BaseModel):

    # required fields
    cpu_usage: List[int]
    memory_total: int  # bytes
    memory_used: int  # bytes
    memory_percentage: float

    # optional fields
    battery_percentage: Optional[float] = None


class ErrorMessage(BaseModel):

    # required fields
    reason: str
