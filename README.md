# MedSpa Booking API

A FastAPI-based booking system for MedSpa appointments with provider abstraction layer.

## Structure

```
medspa_booking_api/
├── app/
│   ├── main.py                 # FastAPI app instance
│   ├── config.py               # Settings
│   ├── dependencies.py         # Dependency injection
│   ├── models/                 # Pydantic models
│   ├── schemas/                # Request/Response schemas
│   ├── routers/                # Route handlers
│   ├── providers/              # Provider abstraction layer
│   ├── services/               # Business logic
│   └── utils/                  # Utilities
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running

```bash
uvicorn app.main:app --reload
```

## API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.

## Provider Pattern

The system uses a provider pattern to abstract different calendar backends:
- `test_provider.py`: Hardcoded test responses
- Future: `gcal_provider.py`, `zenoti_provider.py`, etc.

Configure provider via `PROVIDER` environment variable (defaults to "test"). 