# Pydantic Tutorial

This is a simple FastAPI application that uses Pydantic for data validation.

## Installation

1. Initialize the project:
```bash
uv init
```

2. Install dependencies:
```bash
uv add fastapi uvicorn pydantic pydantic-settings python-dotenv
```

## Running the Application

1. Run the application:
```bash
uvicorn main:app --reload
```

2. Open the application in your browser:
```
http://localhost:8000
```