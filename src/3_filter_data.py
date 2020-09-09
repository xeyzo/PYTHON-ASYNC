import aiohttp
import asyncio
import time
import json
from Fetch import Fetcher as fetcher

url = 'https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json'

async def fetch_url():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    html = await fetcher.get(url)
    loads = json.loads(html)
    filtered1 = filter(lambda x: x['category'] == 'fruits', loads)
    results = list(map(lambda x: f"Nama Buah : {x['name']}", filtered1))
    print("\n".join(results))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_url())