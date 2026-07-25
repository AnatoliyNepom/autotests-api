import asyncio

import websockets
from websockets import ServerConnection


async def echo (websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
        number = 1

        for _ in range(5):
            await websocket.send(f"{number} {response}")
            number += 1


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print ("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())

