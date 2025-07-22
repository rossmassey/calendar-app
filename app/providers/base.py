from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.client import ClientCreate, Client
from app.models.employee import EmployeeCreate, Employee
from app.models.service import Service
from app.models.slot import Slot
from app.models.booking import BookingCreate, BookingResponse, BookingDetail


class BaseProvider(ABC):
    """Abstract base class for calendar providers
    
    Providers accept simple AI-friendly data and internally map to their complex structures.
    They return simple, consistent responses that the AI assistant can easily use.
    """
    
    # Client methods - simple interface for AI
    @abstractmethod
    async def create_client(self, client: ClientCreate) -> Client:
        """Create client using simple AI interface - provider maps to complex structure internally"""
        pass
    
    @abstractmethod
    async def get_client(self, client_id: str) -> Optional[Client]:
        """Return simple client data for AI assistant"""
        pass
    
    @abstractmethod
    async def get_all_clients(self) -> List[Client]:
        """Return simple client list for AI assistant"""
        pass
    
    @abstractmethod
    async def delete_client(self, client_id: str) -> bool:
        pass
    
    # Employee methods - simple interface for AI
    @abstractmethod
    async def create_employee(self, employee: EmployeeCreate) -> Employee:
        """Create employee using simple AI interface - provider maps to complex structure internally"""
        pass
    
    @abstractmethod
    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Return simple employee data for AI assistant"""
        pass
    
    @abstractmethod
    async def get_all_employees(self) -> List[Employee]:
        """Return simple employee list for AI assistant"""
        pass
    
    # Service methods
    @abstractmethod
    async def get_service(self, service_id: str) -> Optional[Service]:
        pass
    
    @abstractmethod
    async def get_all_services(self) -> List[Service]:
        pass
    
    # Slot methods  
    @abstractmethod
    async def get_available_slots(self, customer_id: str, service_id: str, date: str, employee_id: Optional[str] = None) -> List[Slot]:
        """Return available slots for AI assistant"""
        pass
    
    # Booking methods
    @abstractmethod
    async def create_booking(self, booking: BookingCreate) -> BookingResponse:
        pass
    
    @abstractmethod
    async def get_booking(self, booking_id: str) -> Optional[BookingDetail]:
        pass 