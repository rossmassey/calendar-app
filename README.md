# MedSpa Booking API

A simple FastAPI-based booking system for MedSpa appointments with provider abstraction.

## Structure

```
calendar_app/
├── app/
│   ├── main.py                 # FastAPI app
│   ├── config.py               # Settings
│   ├── dependencies.py         # DI
│   ├── models/                 # Pydantic models
│   ├── schemas/                # Response schemas
│   ├── routers/                # API routes
│   ├── providers/              # Provider implementations
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

Visit `http://localhost:8000/docs` for API documentation.

## Provider Pattern

Simple interface for AI assistants that maps to different calendar backends:
- `test_provider.py`: In-memory test implementation
- `zenoti_provider.py`: Stub for Zenoti integration
- Future: Google Calendar, Boulevard, etc.

Configure via `PROVIDER` environment variable (defaults to "test"). 