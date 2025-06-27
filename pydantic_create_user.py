import uuid
from pydantic import BaseModel,Field,EmailStr,ValidationError,constr


class UserSchema(BaseModel):
    """
    Модель пользователя.
    Содержит уникальный идентификатор и основные данные пользователя
    Уникальный ID пользователя
    Email
    Пароль
    Фамилия пользователя
    Имя пользователя
    Отчество пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    password: constr(min_length=8,max_length=255)
    last_name: str = Field(alias ='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

    def get_username(self) -> str:
        """Возвращает полное имя"""
        return f"{self.first_name} {self.last_name}"

    class Config:
        populate_by_name = True

class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя POST /api/v1/users.
    """
    email: EmailStr = Field(default='example@mail.com')
    password: str = Field(default='qwerty12:3')
    last_name: str = Field(alias ='lastName',default='Ivan')
    first_name: str = Field(alias='firstName',default='Ivanov')
    middle_name: str = Field(alias='middleName',default='Ivanov')

class CreateUserResponseSchema(BaseModel):
    """
    Ответ на успешное создание пользователя.
    """
    user: UserSchema


user_data = UserSchema(
    id="id",
    email="Interger@mail.ru",
    password="123456sdsdsdsdsdskfnekd32djjDbjkfdjkfe3232848268247827482378Asd",
    first_name="Tony",
    last_name="Vega",
    middle_name="Ivanovich"
)

default_create_user = CreateUserResponseSchema(user=user_data)
print('default create user: ', default_create_user.model_dump(by_alias=True))

try:
    user = UserSchema(
        id="id",
        email="string@mail.com",
        password="123456sdsdsdsdsdskfnekd32djjDbjkfdjkfe3232848268247827482378Asd",
        first_name="Ivan",
        last_name="Petrov",
        middle_name="Sergeevich"
    )
except ValidationError as error:
    print(error)
    print(error.errors())