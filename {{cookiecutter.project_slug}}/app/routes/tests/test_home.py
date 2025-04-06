import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

# ⬇️ Patch BEFORE anything imports the router
with patch("app.core.auth.roles_required", lambda roles: lambda fn: fn):
    from app.main import app  # <-- router is imported here with patched decorator
    import app.core.dependencies as dependencies
    from app.services.user_service import UserService

def make_sut():
    # Mock the service
    mock_user_service = AsyncMock(spec=UserService)

    # Override the dependency
    app.dependency_overrides[dependencies.get_user_service] = lambda: mock_user_service

    return mock_user_service

# Create a test client
test_client = TestClient(app)

@pytest.mark.asyncio
async def test_get_user_with_mock():
    mock_user_service = make_sut()

    mock_user_service.get_user.return_value = {"id": 1, "name": "Mocked User"}

    response = test_client.get("/user/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Mocked User"}
    mock_user_service.get_user.assert_called_once_with(1)
