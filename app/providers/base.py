from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.client import ClientCreate, Client
from app.models.employee import EmployeeCreate, Employee
from app.models.service import Service
from app.models.slot import Slot
from app.models.booking import BookingCreate, BookingResponse, BookingDetail


class BaseProvider(ABC):
    """Base class for calendar providers"""
    
    @abstractmethod
    async def create_client(self, client: ClientCreate) -> Client:
        pass
    
    @abstractmethod
    async def get_client(self, client_id: str) -> Optional[Client]:
        pass
    
    @abstractmethod
    async def get_all_clients(self) -> List[Client]:
        pass
    
    @abstractmethod
    async def delete_client(self, client_id: str) -> bool:
        pass
    
    @abstractmethod
    async def create_employee(self, employee: EmployeeCreate) -> Employee:
        pass
    
    @abstractmethod
    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        pass
    
    @abstractmethod
    async def get_all_employees(self) -> List[Employee]:
        pass
    
    @abstractmethod
    async def get_service(self, service_id: str) -> Optional[Service]:
        pass
    
    @abstractmethod
    async def get_all_services(self) -> List[Service]:
        pass
    
    @abstractmethod
    async def get_available_slots(self, customer_id: str, service_id: str, date: str, employee_id: Optional[str] = None) -> List[Slot]:
        pass
    
    @abstractmethod
    async def create_booking(self, booking: BookingCreate) -> BookingResponse:
        pass
    
    @abstractmethod
    async def get_booking(self, booking_id: str) -> Optional[BookingDetail]:
        pass 