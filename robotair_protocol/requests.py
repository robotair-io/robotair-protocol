from pydantic import BaseModel
from .compose import ComposeSpecification


class DeploymentUpdateRequest(BaseModel):

    # required fields
    deployment: ComposeSpecification
