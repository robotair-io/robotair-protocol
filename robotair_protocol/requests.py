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


class ServiceStartRequest(BaseModel):

    # NOTE: based on the arguments of
    # https://gabrieldemarmiesse.github.io/python-on-whales/sub-commands/compose/#up

    # required fields
    services: Optional[List[str]]

    # optional fields
    abort_on_container_exit: bool = False
    force_recreate: bool = True
    detach: bool = True
    quiet: bool = True
    remove_orphans: bool = True
    wait: bool = True


class ServiceStopRequest(BaseModel):

    # NOTE: based on the arguments of
    # https://gabrieldemarmiesse.github.io/python-on-whales/sub-commands/compose/#rm

    # required fields
    services: Optional[List[str]]

    # optional fields
    stop: bool = True
