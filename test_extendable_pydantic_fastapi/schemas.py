# Copyright 2023 ACSONE SA/NV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from typing import Generic, TypeVar

from extendable_pydantic.main import ExtendableModelMeta

from pydantic import BaseModel


class User(BaseModel, metaclass=ExtendableModelMeta):
    name: str


class ExtendedUser(User, extends=User):
    address: str


class PrivateUser(User):
    password: str


_T = TypeVar("_T")


class SearchResponse(BaseModel, Generic[_T], metaclass=ExtendableModelMeta):
    total: int
    items: list[_T]


class UserSearchResponse(SearchResponse[User]):
    """We declare the generic type of the items of the list as User
    which is the base model of the extended. When used, it should be resolved
    to ExtendedUser, but items of PrivateUser class must stay private and not be returned"""