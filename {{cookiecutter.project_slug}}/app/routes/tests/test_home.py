from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock
import app.core.dependencies as dependencies
from app.services.user_service import UserService

def make_sut():
    mock_user_service = MagicMock(spec=UserService)
    app.dependency_overrides[dependencies.get_user_service] = lambda: mock_user_service
    return mock_user_service

# Create a test client
test_client = TestClient(app)

def test_get_user_with_mock():
    # Setup SUT
    mock_user_service = make_sut()
    mock_user_service.get_user.return_value = {"id": 1, "name": "Mocked User"}
    
    # Make the request
    response = test_client.get("/user/1")
    
    # Assertions
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Mocked User"}
    mock_user_service.get_user.assert_called_once_with(1)