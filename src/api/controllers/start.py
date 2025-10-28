from http.client import HTTPException

from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix='', tags=["Start"])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_worker_by_id():
    try:
        return {"message": "Hello World!"}
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))
