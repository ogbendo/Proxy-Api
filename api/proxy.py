import asyncio
import more_itertools
import aiohttp

from .urls import *


class Proxies:
    def __init__(self):
        self.randoms = random_proxies
        self.http = http_proxies
        self.socks = socks_proxies

    def getTasks(self, session, urls: list):
        tasks = []
        for url in urls:
            tasks.append(session.get(url, ssl=False))

        return tasks

    async def getProxyList(self, proxy_urls: list):
        proxy_list = []

        async with aiohttp.ClientSession() as session:
            tasks = self.getTasks(session, proxy_urls)
            responses = await asyncio.gather(*tasks)

            for response in responses:
                resp = await response.text()
                proxy_list.append(resp.replace('\r', '').split('\n'))

        return list(more_itertools.flatten(proxy_list))

    async def getRandomProxies(self):
        random_list = await self.getProxyList(self.randoms)
        random_dict = {}
        count = 0

        for proxy in random_list:
            random_dict[count] = proxy
            count += 1

        return random_dict

    async def getHttpProxies(self):
        http_list = await self.getProxyList(self.http)
        http_dict = {}
        count = 0
        for proxy in http_list:
            http_dict[count] = proxy
            count += 1

        return http_dict

    async def getSocksProxies(self):
        socks_list = await self.getProxyList(self.socks)
        socks_dict = {}
        count = 0

        for proxy in socks_list:
            socks_dict[count] = proxy
            count += 1

        return socks_dict



