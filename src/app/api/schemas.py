from uuid import UUID
import pydantic


class ProductSchema(pydantic.BaseModel):
    name: str
    description: str


class ProductGetSchema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None, allow_none=True)
    price: float | None = pydantic.Field(None, allow_none=True)
    image: str | None = pydantic.Field(None, allow_none=True)


class ProductUpdateSchema(pydantic.BaseModel):
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None, allow_none=True)
    price: float | None = pydantic.Field(None, allow_none=True)
    image: str | None = pydantic.Field(None, allow_none=True)


class OrderStatusUpdateSchema(pydantic.BaseModel):
    status: str



