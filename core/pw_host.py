import asyncio
from uuid import uuid4
from playwright.async_api import async_playwright, Browser, Playwright
from ExObject.DateTime import DateTime


class PWHost:
    def __init__(self) -> None:
        self.pw = None
        self.browser = None
        self.pages = {}

    async def create_browser(self):
        self.pw: Playwright = await async_playwright().start()
        self.browser: Browser = await self.pw.chromium.launch()

    async def create_page(self, url, disable_media=True) -> str:
        """
        Create a new page
        return:page_id
        """
        page = await self.browser.new_page()
        if disable_media:
            await page.route(
                "**/*.{png,jpg,jpeg,css,woff2,gif,bmp,webp,mp4,avi,apng,svg,flv,m3u8,mov,wmv,mpeg,webm,mp3,wav,wma}",
                lambda route: route.abort(),
            )
        await page.goto(url, wait_until="commit")
        page_id = str(uuid4())
        self.pages[page_id] = {"page": page, "create": DateTime.Now(), "last_use": DateTime.Now()}
        return page_id

    async def close_page(self, page_id):
        """
        Close a page
        """
        page_info = self.pages.get(page_id)
        if not page_info:
            return
        page = page_info["page"]
        await page.close()
        del self.pages[page_id]

    async def load_url(self, page_id, url):
        page_info = self.pages.get(page_id)
        if not page_info:
            return
        page_info["last_use"] = DateTime.Now()
        page = page_info["page"]
        await page.goto(url, wait_until="commit")

    async def wait_by_selector(self, page_id, selector, timeout=30000):
        page_info = self.pages.get(page_id)
        if not page_info:
            return
        page_info["last_use"] = DateTime.Now()
        page = page_info["page"]
        await page.wait_for_selector(selector, timeout=timeout)

    async def start(self):
        while True:
            await asyncio.sleep(10)
            for page_id, page_info in self.pages.items():
                if DateTime.Now().timestamp() - page_info["last_use"].timestamp() > 60 * 60:
                    await self.close_page(page_id)


if __name__ == "__main__":
    host = PWHost()
    asyncio.run(host.create_browser())
