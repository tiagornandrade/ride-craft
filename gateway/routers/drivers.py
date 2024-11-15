import httpx
from fastapi import APIRouter, HTTPException
from config import DRIVER_SERVICE_URL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/")
async def request_driver(driver_request: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(f"{DRIVER_SERVICE_URL}/drivers/", json=driver_request)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/")
async def get_drivers():
    try:
        logger.debug(f"Requisitando drivers de {DRIVER_SERVICE_URL}/drivers/")
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DRIVER_SERVICE_URL}/drivers/")
        response.raise_for_status()
        logger.debug("Resposta recebida com sucesso.")
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao acessar o serviço de drivers: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

@router.get("/driver/{driver_id}")
async def get_driver(driver_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DRIVER_SERVICE_URL}/drivers/{driver_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
