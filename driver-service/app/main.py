from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/drivers/")
async def list_drivers():
    logger.info("Recebendo requisição GET /drivers/")
    drivers = [{"id": 1, "name": "Driver A"}, {"id": 2, "name": "Driver B"}]
    logger.info(f"Resposta: {drivers}")
    return drivers