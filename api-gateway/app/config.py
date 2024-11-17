import os


DRIVER_SERVICE_URL = os.getenv("DRIVER_SERVICE_URL", "http://driver-service:8001")
RIDE_SERVICE_URL = "http://ride_service:8002"
LOCATION_SERVICE_URL = "http://location_service:8003"
PRICING_SERVICE_URL = "http://pricing_service:8004"
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
