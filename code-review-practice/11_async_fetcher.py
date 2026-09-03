"""
Асинхронный сборщик: тянет JSON с пачки URL «параллельно» и агрегирует.
Живёт в воркере, вызывается на списки в сотни-тысячи адресов.
"""

import asyncio

import httpx


async def fetch_one(client, url):
    resp = client.get(url)
    return resp.json()


async def fetch_all(urls):
    results = []
    for url in urls:
        data = fetch_one(url)
        results.append(data)
    return results


def summarize(urls):
    loop = asyncio.get_event_loop()
    all_data = loop.run_until_complete(fetch_all(urls))

    total = 0
    for d in all_data:
        total += d["count"]
    return total


async def download_report(url):
    async with httpx.AsyncClient() as client:
        data = fetch_one(client, url)
        rows = data["rows"]

        import requests
        extra = requests.get(url + "/extra").json()

        return rows + extra["rows"]
