import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

async def main():
    server = await websockets.serve(echo, "localhost", 8080)

    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
