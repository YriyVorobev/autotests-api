import httpx

login_payload = {
  "email": "use@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
login_response_data = login_response.json()

print('login response:',login_response_data)
print('Status response:', login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization" : f"Bearer {access_token}"
}

access_Token_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
access_Token_response_data = access_Token_response.json()


print('user:',access_Token_response_data)
print('status response:', access_Token_response.status_code)
