from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
import pytest

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()