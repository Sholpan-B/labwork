from uuid import UUID
from starlette import status
import fastapi
from api import schemas

import exceptions.common as common_exc
import exceptions.http as http_exc

from db.repository import ProductRepository

from db.models import Order

# 'api/product':
router = fastapi.APIRouter(prefix='/product', tags=['product'])
repo = ProductRepository()


# Контроллер:
@router.get('')
async def get_products(query: schemas.ProductGetSchema = fastapi.Depends()):
    return await repo.get_list(**query.model_dump(exclude_none=True))


@router.get('/{id}')
async def get_product(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.post('')
async def create_product(body: schemas.ProductSchema):
    try:
        return await repo.create(**body.model_dump(exclude_none=True))

    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.patch('/{id}')
async def update_product(id: UUID, body: schemas.ProductUpdateSchema):
    try:
        return await repo.update(id, **body.model_dump(exclude_none=True))

    except common_exc.UpdateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.delete('/{id}')
async def delete_product(id: UUID):
    try:
        await repo.delete(id)
        return fastapi.responses.Response(status_code=status.HTTP_204_NO_CONTENT)

    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


# Orders
@router.put('/orders/{order_id}/status')
async def update_order_status(order_id: int, order_status: schemas.OrderStatusUpdateSchema):
    try:
        order = await Order.get_or_none(id=order_id)
        order.status = order_status.status
        await order.save()
        return {"message": f"Order status updated to {order_status.status}"}

    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))

    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))




