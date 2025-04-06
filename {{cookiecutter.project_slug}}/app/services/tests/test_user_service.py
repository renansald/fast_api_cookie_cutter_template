import pytest
from app.services.user_service import UserService
from unittest.mock import MagicMock

def make_sut():
    mock_service = MagicMock(spec=UserService)
    return mock_service

@pytest.mark.asyncio
async def test_get_user():
    mock_service = make_sut()
    mock_service.get_user.return_value = {"id": 1, "name": "Mocked User"}
    
    user = await mock_service.get_user(1)
    
    assert user["id"] == 1
    assert user["name"] == "Mocked User"
    mock_service.get_user.assert_called_once_with(1)