import uuid
from typing import List, Optional, Dict, Any
from datetime import datetime, date, time
from decimal import Decimal
from app.providers.base import BaseProvider
from app.models.client import ClientCreate, Client
from app.models.employee import EmployeeCreate, Employee
from app.models.service import Service
from app.models.slot import Slot
from app.models.booking import BookingCreate, BookingResponse, BookingDetail


class TestProvider(BaseProvider):
    """Test provider that accepts simple AI interface and maps internally"""
    
    def __init__(self):
        # Internal storage uses provider's complex structure
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
        """Accept simple AI interface, map internally to test provider structure"""
        client_id = str(uuid.uuid4())
        
        # Internally we might store more complex data, but AI only provides simple data
        internal_client = {
            "id": client_id,
            "name": client.name,
            "phone": client.phone,
            "email": client.email,
            "created_at": datetime.utcnow().isoformat(),
            # Test provider might track additional internal fields
            "membership_level": "Standard",
            "visit_count": 0
        }
        
        self.clients[client_id] = internal_client
        
        # Return simple response for AI
        return Client(
            id=client_id,
            name=client.name,
            phone=client.phone,
            email=client.email
        )
    
    async def get_client(self, client_id: str) -> Optional[Client]:
        """Return simple client data for AI - hide internal complexity"""
        internal_client = self.clients.get(client_id)
        if not internal_client:
            return None
            
        # Reduce complex internal data to simple AI interface
        return Client(
            id=internal_client["id"],
            name=internal_client["name"],
            phone=internal_client["phone"],
            email=internal_client["email"]
        )
    
    async def get_all_clients(self) -> List[Client]:
        """Return simple client list for AI"""
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
        """Accept simple AI interface, map internally to test provider structure"""
        employee_id = str(uuid.uuid4())
        
        # Internally store in test provider's format
        internal_employee = {
            "id": employee_id,
            "name": employee.name,
            "center_id": employee.center_id,
            "phone": employee.phone,
            "specialties": employee.specialties,
            "is_available": True,
            # Test provider internal fields
            "hire_date": datetime.utcnow().isoformat(),
            "status": "active"
        }
        
        self.employees[employee_id] = internal_employee
        
        # Return simple response for AI
        return Employee(
            id=employee_id,
            name=employee.name,
            center_id=employee.center_id,
            specialties=employee.specialties,
            phone=employee.phone,
            is_available=True
        )
    
    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Return simple employee data for AI - hide internal complexity"""
        internal_employee = self.employees.get(employee_id)
        if not internal_employee:
            return None
            
        # Reduce complex internal data to simple AI interface
        return Employee(
            id=internal_employee["id"],
            name=internal_employee["name"],
            center_id=internal_employee["center_id"],
            specialties=internal_employee["specialties"],
            phone=internal_employee["phone"],
            is_available=internal_employee["is_available"]
        )
    
    async def get_all_employees(self) -> List[Employee]:
        """Return simple employee list for AI"""
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
        """Return simple slots for AI"""
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