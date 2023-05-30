from pydantic import BaseModel
from typing import List, Optional
from .compose import ComposeSpecification


class DeploymentUpdateRequest(BaseModel):

    # required fields
    deployment: ComposeSpecification


class ImagePullRequest(BaseModel):

    # NOTE: based on the arguments of
    # https://gabrieldemarmiesse.github.io/python-on-whales/sub-commands/compose/#pull

    # required fields
    services: Optional[List[str]]

    # optional fields
    ignore_pull_failures: bool = False
    include_deps: bool = True
    quiet: bool = True
