import aiohttp
import asyncio
import time
import json
from Fetch import Fetcher as fetcher

urls = 'https://jsonplaceholder.typicode.com/posts'

async def fetch_url():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    html = await fetcher.get(urls)
    loads = json.loads(html)
    print('\n'.join(list(map(lambda loads: f"{loads['title']}", loads))))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_url())