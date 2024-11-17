import httpx
from fastapi import APIRouter, HTTPException, Request
from config import DRIVER_SERVICE_URL, REDIS_HOST, REDIS_PORT
import logging
from slowapi import Limiter
from slowapi.util import get_remote_address
import redis


redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

limiter = Limiter(key_func=get_remote_address)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/")
@limiter.limit("5 per minute")
async def request_driver(request: Request, driver_request: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(f"{DRIVER_SERVICE_URL}/drivers/", json=driver_request)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Timeout reached while trying to connect to driver service")

@router.get("/")
@limiter.limit("5 per minute")
async def get_drivers(request: Request):
    try:
        logger.debug(f"Requisitando drivers de {DRIVER_SERVICE_URL}/drivers/")
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DRIVER_SERVICE_URL}/drivers/")
            response.raise_for_status()
        logger.debug(f"Resposta recebida: {response.json()}")
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao acessar o serviço de drivers: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
    except httpx.RequestError as e:
        logger.error(f"Erro ao fazer a requisição HTTP: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a requisição: {str(e)}")
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


@router.get("/driver/{driver_id}")
@limiter.limit("5 per minute")
async def get_driver(request: Request, driver_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DRIVER_SERVICE_URL}/drivers/{driver_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
