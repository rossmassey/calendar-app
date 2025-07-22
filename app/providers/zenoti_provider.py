from typing import List, Optional
from datetime import datetime, time
from decimal import Decimal
from app.providers.base import BaseProvider
from app.models.client import ClientCreate, Client
from app.models.employee import EmployeeCreate, Employee
from app.models.service import Service
from app.models.slot import Slot
from app.models.booking import BookingCreate, BookingResponse, BookingDetail


class ZenotiProvider(BaseProvider):
    """Zenoti provider that accepts simple AI interface and maps to complex Zenoti API internally"""
    
    async def create_client(self, client: ClientCreate) -> Client:
        """Accept simple AI data, map to complex Zenoti structure internally"""
        
        # Map simple AI input to complex Zenoti API call
        zenoti_request = {
            "first_name": client.name.split()[0] if client.name else "Unknown",
            "last_name": " ".join(client.name.split()[1:]) if client.name and len(client.name.split()) > 1 else "",
            "mobile_number": client.phone or "",
            "email": client.email or "",
            "gender": "Other",  # Default since AI doesn't provide this
            "center_id": "default_center",  # Use default since AI doesn't specify
            "membership_type": "Regular",  # Default
            "source": "API"
        }
        
        # In real implementation: zenoti_response = await call_zenoti_api("/guests", zenoti_request)
        zenoti_response = {
            "guest_id": "ZEN123456", 
            "full_name": client.name,
            "phone": client.phone,
            "email": client.email,
            "membership_level": "Silver",
            "loyalty_points": 0
        }
        
        # Reduce complex Zenoti response to simple AI interface
        return Client(
            id=zenoti_response["guest_id"],
            name=zenoti_response["full_name"], 
            phone=zenoti_response["phone"],
            email=zenoti_response["email"]
        )
    
    async def create_employee(self, employee: EmployeeCreate) -> Employee:
        """Accept simple AI data, map to complex Zenoti structure internally"""
        
        # Map simple AI input to complex Zenoti API structure
        zenoti_request = {
            "employee_code": f"EMP{hash(employee.name) % 10000:04d}",  # Auto-generate
            "first_name": employee.name.split()[0] if employee.name else "Unknown",
            "last_name": " ".join(employee.name.split()[1:]) if employee.name and len(employee.name.split()) > 1 else "",
            "email": f"{employee.name.lower().replace(' ', '.')}@spa.com",  # Auto-generate
            "mobile_number": employee.phone or "",
            "designation": "Therapist",  # Default role
            "center_id": employee.center_id,
            "commission_percentage": 30.0,  # Default commission
            "service_categories": employee.specialties,  # Map specialties directly
            "working_hours": {  # Default schedule
                "monday": "09:00-17:00",
                "tuesday": "09:00-17:00", 
                "wednesday": "09:00-17:00",
                "thursday": "09:00-17:00",
                "friday": "09:00-17:00"
            },
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "employee_type": "full_time",
            "is_active": True
        }
        
        # In real implementation: zenoti_response = await call_zenoti_api("/employees", zenoti_request)
        zenoti_response = {
            "staff_id": f"ST{zenoti_request['employee_code']}",
            "display_name": f"{zenoti_request['first_name']} {zenoti_request['last_name']}",
            "email": zenoti_request["email"],
            "phone": zenoti_request["mobile_number"],
            "specializations": zenoti_request["service_categories"],
            "center_id": zenoti_request["center_id"],
            "is_active": True
        }
        
        # Reduce complex Zenoti response to simple AI interface
        return Employee(
            id=zenoti_response["staff_id"],
            name=zenoti_response["display_name"],
            center_id=zenoti_response["center_id"],
            specialties=zenoti_response["specializations"],
            phone=zenoti_response["phone"],
            is_available=zenoti_response["is_active"]
        )
    
    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Fetch from Zenoti and reduce to simple AI interface"""
        # In real implementation: zenoti_response = await call_zenoti_api(f"/employees/{employee_id}")
        zenoti_response = {
            "staff_id": employee_id,
            "display_name": "Sarah Johnson",
            "email": "sarah@spa.com",
            "phone": "555-0123",
            "specializations": ["Facial", "Chemical Peels"],
            "center_id": "center_001",
            "commission_rate": 0.40,
            "schedule": {"monday": "09:00-17:00"},
            "employment_status": "full_time",
            "is_active": True
        }
        
        # Reduce complex Zenoti data to simple AI interface
        return Employee(
            id=zenoti_response["staff_id"],
            name=zenoti_response["display_name"],
            center_id=zenoti_response["center_id"],
            specialties=zenoti_response["specializations"],
            phone=zenoti_response["phone"],
            is_available=zenoti_response["is_active"]
        )
    
    # Simplified implementations for other methods
    async def get_client(self, client_id: str) -> Optional[Client]:
        # Mock Zenoti response reduced to simple AI interface
        return Client(
            id=client_id,
            name="John Doe",
            phone="+1234567890",
            email="john@example.com"
        )
    
    async def get_all_clients(self) -> List[Client]:
        return []
    
    async def delete_client(self, client_id: str) -> bool:
        return True
        
    async def get_all_employees(self) -> List[Employee]:
        return []
    
    async def get_service(self, service_id: str) -> Optional[Service]:
        return Service(
            id=service_id,
            service_name="Facial",
            price=Decimal("150.00"),
            duration=60
        )
    
    async def get_all_services(self) -> List[Service]:
        return []
    
    async def get_available_slots(self, customer_id: str, service_id: str, date: str, employee_id: Optional[str] = None) -> List[Slot]:
        return []
    
    async def create_booking(self, booking: BookingCreate) -> BookingResponse:
        return BookingResponse(
            id="booking-123",
            slot_id=booking.slot_id,
            status="reserved", 
            expires_at=datetime.now()
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