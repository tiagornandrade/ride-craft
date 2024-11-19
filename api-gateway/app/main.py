from fastapi import FastAPI, Depends
from auth import JWTBearer
from routers import drivers, rides, locations, pricings
from middlewares import LoggingMiddleware, AddHeadersMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Mobility API Gateway")
Instrumentator().instrument(app).expose(app)

app.add_middleware(LoggingMiddleware)
app.add_middleware(AddHeadersMiddleware)

app.include_router(drivers.router, prefix="/drivers", dependencies=[Depends(JWTBearer())])
app.include_router(rides.router, prefix="/rides", dependencies=[Depends(JWTBearer())])
app.include_router(locations.router, prefix="/locations", dependencies=[Depends(JWTBearer())])
app.include_router(pricings.router, prefix="/pricings", dependencies=[Depends(JWTBearer())])
