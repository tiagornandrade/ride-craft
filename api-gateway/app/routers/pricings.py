import httpx
from fastapi import APIRouter, HTTPException
from config import PRICING_SERVICE_URL

router = APIRouter()


@router.post("/")
async def request_pricing(pricing_request: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.post(f"{PRICING_SERVICE_URL}/pricings/", json=pricing_request)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/")
async def get_pricings():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.get(f"{PRICING_SERVICE_URL}/pricings/")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/pricing/{pricing_id}")
async def get_pricing(pricing_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.get(f"{PRICING_SERVICE_URL}/pricings/{pricing_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
