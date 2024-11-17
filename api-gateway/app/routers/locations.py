import httpx
from fastapi import APIRouter, HTTPException
from config import LOCATION_SERVICE_URL

router = APIRouter()


@router.post("/")
async def request_location(location_request: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await http.post(f"{LOCATION_SERVICE_URL}/locations/", json=location_request)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/")
async def get_locations():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await http.get(f"{LOCATION_SERVICE_URL}/locations/")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/location/{location_id}")
async def get_location(location_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await http.get(f"{LOCATION_SERVICE_URL}/locations/{location_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
