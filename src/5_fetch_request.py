import aiohttp
import asyncio
import time
import json
from Fetch import Fetcher as fetcher

url1 = 'https://jsonplaceholder.typicode.com/posts'
url2 = 'https://jsonplaceholder.typicode.com/users'

async def fetch_url():
    start = time.time()
    print(f"started at {time.strftime('%X')}")
    
    html1 = await fetcher.get(url1)
    html2 = await fetcher.get(url2)
    loads1 = json.loads(html1)
    loads2 = json.loads(html2)
    async def user(id):
        return list(filter(lambda a: a['id'] == id, loads2))[0]

    for post in loads1:
        # filter data posts yang idnya sesuai dengan data users
        post['user'] = await user(post['userId'])
        # dirapikan tampilan saat dieksekusi
        print(json.dumps(post, indent=4))
    
    end = time.time()
    print(f"Finished at {time.strftime('%X')}")
    print(f"Total time: {round(int(end - start))}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_url())