from fastapi import HTTPException


class ClientNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Client not found")


class ServiceNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Service not found")


class CenterNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Center not found")


class EmployeeNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Employee not found")


class SlotNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Slot not found")


class BookingNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Booking not found") 