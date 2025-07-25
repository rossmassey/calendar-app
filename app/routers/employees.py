from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.employee import EmployeeCreate, Employee
from app.schemas.employee import EmployeeResponse
from app.providers.base import BaseProvider
from app.dependencies import get_provider

router = APIRouter()


@router.post("/", response_model=EmployeeResponse)
async def create_employee(
    employee: EmployeeCreate,
    provider: BaseProvider = Depends(get_provider)
):
    """Create an employee"""
    result = await provider.create_employee(employee)
    return EmployeeResponse(
        id=result.id,
        center_name=result.center_id,
        zip_code="Unknown",
        time_zone="Unknown"
    )


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(
    employee_id: str,
    provider: BaseProvider = Depends(get_provider)
):
    """Get an employee"""
    employee = await provider.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return EmployeeResponse(
        id=employee.id,
        center_name=employee.center_id,
        zip_code="Unknown",
        time_zone="Unknown"
    )


@router.get("/", response_model=List[EmployeeResponse])
async def get_all_employees(
    provider: BaseProvider = Depends(get_provider)
):
    """Get all employees"""
    employees = await provider.get_all_employees()
    return [
        EmployeeResponse(
            id=employee.id,
            center_name=employee.center_id,
            zip_code="Unknown",
            time_zone="Unknown"
        )
        for employee in employees
    ]


@router.get("/schema")
async def get_employee_schema():
    """Get the schema for creating employees"""
    return {
        "schema": EmployeeCreate.model_json_schema(),
        "example": {
            "name": "Sarah Johnson",
            "center_id": "1", 
            "specialties": ["Botox", "Facials"],
            "phone": "555-0123"
        }
    } 