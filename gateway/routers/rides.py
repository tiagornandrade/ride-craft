import httpx
from fastapi import APIRouter, HTTPException
from config import RIDE_SERVICE_URL

router = APIRouter()


@router.post("/")
async def request_ride(ride_request: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.post(f"{RIDE_SERVICE_URL}/rides/", json=ride_request)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/")
async def get_rides():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.post(f"{RIDE_SERVICE_URL}/rides/")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())

@router.get("/ride/{ride_id}")
async def get_ride(ride_id: str):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await httpx.get(f"{RIDE_SERVICE_URL}/rides/{ride_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
