from pydantic import BaseModel
from typing import List, Optional
from .compose import ComposeSpecification


class DeploymentRegisterRequest(BaseModel):

    # required fields
    identifier: str
    deployment: ComposeSpecification


class DeploymentRevertRequest(BaseModel):

    pass


class DeploymentUpdateRequest(BaseModel):

    pass


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


class RegistryLoginRequest(BaseModel):

    # NOTE: based on the arguments of
    # https://gabrieldemarmiesse.github.io/python-on-whales/docker_client/#login

    # required fields
    server: str
    username: str
    password: str


class RegistryLogoutRequest(BaseModel):

    # NOTE: based on the arguments of
    # https://gabrieldemarmiesse.github.io/python-on-whales/docker_client/#logout

    # required fields
    server: str
