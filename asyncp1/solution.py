import asyncio
import httpx


async def fetch(url, client):
    # TODO return url and response.text
    pass


async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        # TODO implement the logic here
        # return a dict of url and content
        pass
