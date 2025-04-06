
# FastAPI Cookiecutter Template

This template automates the creation of a production-ready FastAPI project using Cookiecutter. It includes Inversion of Control (IoC), Dependency Injection (DI), Okta authentication, structured logging with Azure Application Insights, and testing support.

## 🚀 Features
- **FastAPI** web framework
- **IoC and Dependency Injection** via dependency-injector
- **Environment Configuration** using .env
- **OAuth2 Authentication** with **Okta**
- **Role-Based Authorization** with a custom decorator
- **Structured Logging** with Loguru + Azure Application Insights
- **Testing Suite** with pytest
- **Code Formatting & Linting** with black and ruff
- **Docker Support** with a multi-stage setup
- **Poetry** for dependency and script management


## Installation & Usage

### 💠 Prerequisites
- Python 3.12+
- Poetry
- Cookiecutter

### 🧱 Generate a New Project
Run the following command to create a new FastAPI project:

```sh
cookiecutter https://github.com/renansald/fast_api_cookie_cutter_template.git
```

Follow the prompts to customize your project.

### 📦 Install Dependencies
#### Enable virtaul env

```sh
poetry shell
```

#### Base Dependencies

```sh
cd my_fastapi_project
poetry install
```
#### Install Dev and Test Dependencies

To install development and testing tools (e.g., pytest, black, ruff):

```sh
poetry install --with dev,test
```

## Run the Application
To start the application locally:

```sh
poetry run uvicorn app.main:app --reload
```

You can also install them separately if needed:
```sh
poetry install --with dev
poetry install --with test
```

### 🥪 Running the Application

#### Start the Development Server

```sh
poetry run uvicorn app.main:app --reload
```

##### Run Tests

```sh
poetry run pytest
```

#### Generate test coverage report:

```sh
poetry run pytest --cov=app --cov-report=html
```
### 🧹 Code Quality & Formatting

#### Format Code with black

```sh
poetry run black .
```
#### Lint Code with ruff

```sh
poetry run ruff check .
```
#### You can also autofix issues with:

```sh
poetry run ruff check . --fix
```
## 🗂️ Project Structure

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

## 🧬Environment Variables

Create a `.env` file and define the required variables:

```
APP_NAME="MyFastAPIApp"
DEBUG="True"
DATABASE_URL="sqlite:///./production.db"
OKTA_DOMAIN="https://your-okta-domain.okta.com"
OKTA_AUDIENCE="your-api-audience"
```

## 🔐 Authentication & Authorization

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

## 🐳 Docker Support

### Build and Run

Build the Docker image:

```sh
docker build -t my_fastapi_app .
```

Run the container:

```sh
docker run -p 8000:8000 my_fastapi_app
```

## 🤝 Contributing

Feel free to contribute to this template by submitting issues and pull requests.

## 📄 License

This project is licensed under the MIT License.