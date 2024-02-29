import aiohttp
import asyncio

async def send_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(f"[x] {url} - {response.status}")
            return response