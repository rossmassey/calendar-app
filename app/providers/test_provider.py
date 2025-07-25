import uuid
from typing import List, Optional, Dict, Any
from datetime import datetime, time
from decimal import Decimal
from app.providers.base import BaseProvider
from app.models.client import ClientCreate, Client
from app.models.employee import EmployeeCreate, Employee
from app.models.service import Service
from app.models.slot import Slot
from app.models.booking import BookingCreate, BookingResponse, BookingDetail


class TestProvider(BaseProvider):
    """Test provider with hardcoded responses"""
    
    def __init__(self):
        self.clients: Dict[str, Dict[str, Any]] = {}
        self.employees: Dict[str, Dict[str, Any]] = {
            "1": {
                "id": "1",
                "name": "Sarah Johnson",
                "center_id": "1",
                "phone": "555-0123",
                "specialties": ["Botox", "Facials"],
                "is_available": True
            },
            "2": {
                "id": "2",
                "name": "Mike Chen", 
                "center_id": "1", 
                "phone": "555-0456",
                "specialties": ["Massage", "Wellness"],
                "is_available": True
            }
        }
        self.services: Dict[str, Dict[str, Any]] = {
            "1": {
                "id": "1",
                "service_name": "Botox Treatment",
                "price": Decimal("300.00"),
                "duration": 60
            },
            "2": {
                "id": "2", 
                "service_name": "Facial",
                "price": Decimal("150.00"),
                "duration": 90
            }
        }
    
    async def create_client(self, client: ClientCreate) -> Client:
        client_id = str(uuid.uuid4())
        internal_client = {
            "id": client_id,
            "name": client.name,
            "phone": client.phone,
            "email": client.email,
            "created_at": datetime.utcnow().isoformat()
        }
        self.clients[client_id] = internal_client
        
        return Client(
            id=client_id,
            name=client.name,
            phone=client.phone,
            email=client.email
        )
    
    async def get_client(self, client_id: str) -> Optional[Client]:
        client = self.clients.get(client_id)
        if not client:
            return None
        return Client(
            id=client["id"],
            name=client["name"],
            phone=client["phone"],
            email=client["email"]
        )
    
    async def get_all_clients(self) -> List[Client]:
        return [
            Client(
                id=client["id"],
                name=client["name"],
                phone=client["phone"],
                email=client["email"]
            )
            for client in self.clients.values()
        ]
    
    async def delete_client(self, client_id: str) -> bool:
        if client_id in self.clients:
            del self.clients[client_id]
            return True
        return False
    
    async def create_employee(self, employee: EmployeeCreate) -> Employee:
        employee_id = str(uuid.uuid4())
        internal_employee = {
            "id": employee_id,
            "name": employee.name,
            "center_id": employee.center_id,
            "phone": employee.phone,
            "specialties": employee.specialties,
            "is_available": True
        }
        self.employees[employee_id] = internal_employee
        
        return Employee(
            id=employee_id,
            name=employee.name,
            center_id=employee.center_id,
            specialties=employee.specialties,
            phone=employee.phone,
            is_available=True
        )
    
    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        employee = self.employees.get(employee_id)
        if not employee:
            return None
        return Employee(
            id=employee["id"],
            name=employee["name"],
            center_id=employee["center_id"],
            specialties=employee["specialties"],
            phone=employee["phone"],
            is_available=employee["is_available"]
        )
    
    async def get_all_employees(self) -> List[Employee]:
        return [
            Employee(
                id=emp["id"],
                name=emp["name"],
                center_id=emp["center_id"],
                specialties=emp["specialties"],
                phone=emp["phone"],
                is_available=emp["is_available"]
            )
            for emp in self.employees.values()
        ]
    
    async def get_service(self, service_id: str) -> Optional[Service]:
        service = self.services.get(service_id)
        if not service:
            return None
        return Service(**service)
    
    async def get_all_services(self) -> List[Service]:
        return [Service(**service) for service in self.services.values()]
    
    async def get_available_slots(self, customer_id: str, service_id: str, date: str, employee_id: Optional[str] = None) -> List[Slot]:
        return [
            Slot(
                id="1",
                center_id="1", 
                service_id=service_id,
                date=date,
                start_time=time(9, 0),
                end_time=time(10, 0),
                employee_id=employee_id or "1",
                price=Decimal("300.00"),
                currency="USD"
            )
        ]
    
    async def create_booking(self, booking: BookingCreate) -> BookingResponse:
        booking_id = str(uuid.uuid4())
        return BookingResponse(
            id=booking_id,
            slot_id=booking.slot_id,
            status="reserved",
            expires_at=datetime.utcnow()
        )
    
    async def get_booking(self, booking_id: str) -> Optional[BookingDetail]:
        return BookingDetail(
            id=booking_id,
            status="confirmed",
            service_id="1",
            employee_id="1",
            start_time=time(9, 0),
            end_time=time(10, 0)
        ) 