from fastapi import FastAPI
from app.routers import clients, services, centers, employees, slots, bookings
from app.config import settings

app = FastAPI(
    title="MedSpa Booking API",
    description="API for managing MedSpa appointments",
    version="1.0.0"
)

# Include routers (like Django URL includes)
app.include_router(clients.router, prefix="/api/v1/clients", tags=["clients"])
app.include_router(services.router, prefix="/api/v1/services", tags=["services"])
app.include_router(centers.router, prefix="/api/v1/centers", tags=["centers"])
app.include_router(employees.router, prefix="/api/v1/employees", tags=["employees"])
app.include_router(slots.router, prefix="/api/v1/slots", tags=["slots"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["bookings"])

@app.get("/")
async def root():
    return {"message": "MedSpa Booking API"} 