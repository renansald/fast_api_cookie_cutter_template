
# FastAPI Cookiecutter Template

This template automates the creation of a FastAPI project with Inversion of Control (IoC), Dependency Injection (DI), authentication via Okta, and test support using Cookiecutter.

## Features
- **FastAPI** framework
- **IoC and Dependency Injection** using `dependency-injector`
- **Environment Configuration** via `.env` file
- **OAuth2 Authentication** with Okta
- **Role-Based Authorization** decorator
- **Testing** using `pytest` with structured test directories
- **Docker Support** with multi-stage build and run setup
- **Poetry Package Management** with predefined scripts

## Installation & Usage

### Prerequisites
- Python 3.12+
- Poetry
- Cookiecutter

### Generate a New Project
Run the following command to create a new FastAPI project:

```sh
cookiecutter https://github.com/your-repo/fastapi-template.git
```

Follow the prompts to customize your project.

### Install Dependencies
Navigate to your newly created project and install dependencies:

```sh
cd my_fastapi_project
poetry install
```

### Run the Application
To start the application locally:

```sh
poetry run uvicorn app.main:app --reload
```

### Run Tests
Run the test suite with:

```sh
poetry run pytest
```

Generate test coverage report:

```sh
poetry run pytest --cov=app --cov-report=html
```

## Project Structure

```
my_fastapi_project/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── routers/                # API route handlers
│   ├── models/                 # Data models
│   ├── services/               # Business logic
│   ├── core/
│   │   ├── config.py           # Load settings from .env
│   │   ├── auth.py             # Okta authentication and authorization
|   |   |-- app_insigths.py     # APP insights configuration
│   |   |-- dependencies.py     # Dependency injection setup
│   |   |-- containers.py       # IoC container
|   |   |-- logging_config.py   # loggers configuration with loguru
├── tests/                      # Test suite
├── .gitignore
├── README.md
├── pyproject.toml              # Poetry configuration
├── Dockerfile                  # Docker setup
├── .env                        # Environment variables (not committed)
```

## Environment Variables

Create a `.env` file and define the required variables:

```
APP_NAME="MyFastAPIApp"
DEBUG="True"
DATABASE_URL="sqlite:///./production.db"
OKTA_DOMAIN="https://your-okta-domain.okta.com"
OKTA_AUDIENCE="your-api-audience"
```

## Authentication & Authorization

- Uses Okta for authentication.
- `roles_required` decorator restricts access to specified roles.

Example usage:

```python
from fastapi import APIRouter
from app.core.auth import roles_required

router = APIRouter()

@router.get("/admin")
@roles_required(["admin"])
async def admin_dashboard():
    return {"message": "Welcome, admin!"}
```

## Docker Support

### Build and Run

Build the Docker image:

```sh
docker build -t my_fastapi_app .
```

Run the container:

```sh
docker run -p 8000:8000 my_fastapi_app
```

## Contributing

Feel free to contribute to this template by submitting issues and pull requests.

## License

This project is licensed under the MIT License.