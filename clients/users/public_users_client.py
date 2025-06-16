from clients.api_client import APIClient

from httpx import Response

from typing import TypedDict


class CreateUsersRequest(TypedDict):
    """
    Описание структуры запроса на создание публичного пользователя
    """
    email: str
    password : str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """Клиент для работы /api/v1/users
    """
    def create_user_api(self,
        request: CreateUsersRequest )-> Response:
        """
        Метод выполняет создание публичного пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.post("/api/v1/users",json=request)

