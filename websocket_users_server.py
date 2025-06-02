import asyncio

import websockets

from websockets import ServerConnection

async def echo(websocket:ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for _ in range(1,6):
            response = f" Сервер получил: {message}"
            await websocket.send(response)
            print(f"Отправлено сообщение {response}")


async def main():
    server = await websockets.serve(echo,"localhost",8765)
    print("Websocket сервер запущен на ws//localhost:8765")
    await server.wait_closed()

asyncio.run(main())