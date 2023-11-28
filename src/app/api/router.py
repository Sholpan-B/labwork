import fastapi
from api.product.routes import router as product_router
from adapters import MinIOClient
from starlette import status


router = fastapi.APIRouter(prefix='/api')

router.include_router(product_router)


@router.post('/upload')
async def upload_file(file: fastapi.UploadFile = fastapi.File(...)):
    client = MinIOClient()
    await client.upload_from_bytes(file)

    return fastapi.Response(status_code=status.HTTP_204_NO_CONTENT)



