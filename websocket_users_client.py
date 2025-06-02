import asyncio

import websockets



async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input('Введите ваше сообщение: ')
        print(f"Отправка: {message}")
        await websocket.send(message)

        for _ in range(1,6):
            response = await websocket.recv()
            print(f" {_} Сообщение пользователя: {response}")

asyncio.run(client())


