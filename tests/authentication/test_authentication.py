from http import HTTPStatus
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from fixtures.users import UserFixture
import pytest


@pytest.mark.authentication
@pytest.mark.regression
class TestAuthentication:
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        request = CreateUserRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())