from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
# from pydantic.generics import GenericModel

# T = TypeVar('T')

class MenuSchema(BaseModel):
	id: Optional[int]=None
	title: Optional[str]=None
	description: Optional[str]=None

	class Config:
		orm_mode = True


class RequestMenu(BaseModel):
	parameter: MenuSchema = Field(...)


class SubMenuSchema(BaseModel):
	id: Optional[int]=None
	title: Optional[str]=None
	description: Optional[str]=None

	class Config:
		orm_mode = True


class RequestSubMenu(BaseModel):
	parameter: SubMenuSchema = Field(...)


class DishesSchema(BaseModel):
	id: Optional[int]=None
	title: Optional[str]=None
	description: Optional[str]=None

	class Config:
		orm_mode = True


class RequestDishes(BaseModel):
	parameter: DishesSchema = Field(...)	


class Response(BaseModel, Generic[T]):
	code: str
	status: str
	message: str
	result: Optional[T]


