from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import clients, services, centers, employees, slots, bookings, cityglow_florida

app = FastAPI(
    title="MedSpa Booking API",
    description="API for managing MedSpa appointments and City Glow Florida services",
    version="1.0.0"
)

API_PREFIX = "/api/v1"

# Existing calendar app routes
app.include_router(clients.router, prefix=f"{API_PREFIX}/clients", tags=["clients"])
app.include_router(services.router, prefix=f"{API_PREFIX}/services", tags=["services"])
app.include_router(centers.router, prefix=f"{API_PREFIX}/centers", tags=["centers"])
app.include_router(employees.router, prefix=f"{API_PREFIX}/employees", tags=["employees"])
app.include_router(slots.router, prefix=f"{API_PREFIX}/slots", tags=["slots"])
app.include_router(bookings.router, prefix=f"{API_PREFIX}/bookings", tags=["bookings"])

# City Glow Florida routes
app.include_router(cityglow_florida.router, prefix=f"{API_PREFIX}/cityglow_florida", tags=["cityglow_florida"])

@app.get("/")
async def root():
    return {
        "status": "ok",
    }
