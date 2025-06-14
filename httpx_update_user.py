

import httpx

from tools.fakers import get_random_email

# Создаем пользователя

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_payload_response = httpx.post("http://127.0.0.1:8000/api/v1/users",json=create_user_payload)
create_user_payload_data = create_user_payload_response.json()

print("Create user: ", create_user_payload_data)
print("response code: ", create_user_payload_response.status_code)

# Проходим аутентификацию
login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}

login_response_user = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login",json=login_payload)
login_response_user_data = login_response_user.json()

print("login_data",login_response_user_data)
print("response code:",login_response_user.status_code)

# Изменяем данные пользователя
path_user_header = {
  "Authorization": f"Bearer {login_response_user_data['token']['accessToken']}"
}
path_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
path_user_response = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_payload_data['user']['id']}",
                     headers= path_user_header,json=path_payload)
path_user_response_data = path_user_response.json()
print("response update:", path_user_response_data)
print("response code:", path_user_response.status_code)