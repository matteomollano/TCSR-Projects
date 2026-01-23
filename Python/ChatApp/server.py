import asyncio
import websockets

clients = set()

# async/await
# part of app that relies on data you are awaiting is blocked, but rest of app is free to continue working
# we don't want to block the server while waiting
async def handle(ws):
    clients.add(ws)
    try:
        async for msg in ws:
            tasks = []
            for c in clients:
                if c != ws:
                    tasks.append(c.send(msg))
            await asyncio.gather(*tasks)
    except websockets.exceptions.ConnectionClosed:
        print("You cannot connect because the connection is closed.")
    finally:
        clients.remove(ws)

async def main():
    async with websockets.serve(handle, "192.168.5.226", 6789):
        print("Server running at ws://192.168.5.226:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())