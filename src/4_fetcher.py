import json
import asyncio
import aiohttp
import time
from Fetch import Fetcher as fetcher

async def fetch_url():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    jsonData ={
        "id": 30,
        "name": "Someone"
    }
    
    html = await fetcher.get("https://httpbin.org/get")
    html2 = await fetcher.delete("https://httpbin.org/delete")
    html3 = await fetcher.post("https://httpbin.org/post", jsonData)
    loads = json.loads(html)
    loads2 = json.loads(html2)
    loads3 = json.loads(html3)
    print(json.dumps(loads, indent=4))
    print(json.dumps(loads2, indent=4))
    print(json.dumps(loads3, indent=4))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_url())