# playwright install chromium
# CENTOS: yum -y install libX11 libXcomposite libXcursor libXdamage libXext libXi libXtst cups-libs libXScrnSaver libXrandr alsa-lib pango atk at-spi2-atk gtk3
# CENTOS: yum -y install chromium
import asyncio
from playwright.async_api import async_playwright, Page, Browser
from ExObject.ExParsel import ExSelector
from ExObject.DateTime import DateTime
import uuid


async def load_handler(page: Page):
    await page.route("**/*.{png,jpg,jpeg,css,woff2,gif}", lambda route: route.abort())


async def load_page(browser: Browser, url):
    page = await browser.new_page()
    await load_handler(page)
    await page.goto(url, wait_until="commit")
    await page.wait_for_selector("img", state="attached", timeout=1000 * 100)
    # await page.get_by_role("h1").check(timeout=1000 * 100)
    await page.screenshot(path="./temp/" + str(uuid.uuid4()) + ".png")
    await page.close()


async def main():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(proxy={"server": "http://192.168.31.102:7890"})
        browser = await p.chromium.launch()

        # tasks = [
        #     load_page(browser, "https://www.baidu.com"),
        #     load_page(browser, "https://www.qq.com/"),
        #     load_page(browser, "https://www.163.com/"),
        #     load_page(browser, "https://www.sina.com.cn/"),
        #     load_page(browser, "https://www.bilibili.com/"),
        #     load_page(browser, "https://www.12306.cn/index/"),
        #     load_page(browser, "https://mos.m.taobao.com/union/jhsjx2020?pid=mm_43125636_4246598_109944300468"),
        #     load_page(
        #         browser,
        #         "https://www.jd.com/?cu=true&utm_source=www.hao123.com&utm_medium=tuiguang&utm_campaign=t_1000003625_hao123mz&utm_term=8b012924ccf14db594a83b9172777d7c",
        #     ),
        #     load_page(
        #         browser,
        #         "https://www.tmall.com/?ali_trackid=2:mm_43125636_4246598_115687200148:1718876636_059_1137627463&union_lens=lensId:OPT@1664442660@0bb1cee3_0a80_1838883766d_d3e5@01;eventPageId:20150318020013285;recoveryid:059_743605654@1718876636006&pageId=20150318020013285&rootPageId=20150318020013285&bxsign=tbkksm7f8uphoFtzbbzfXzgM6svBXmsEAX2UK1eHvTf_35pSQS7ObMcjI8yNILb50G-QpKg_G5sUMh5OkEKmDXfSi0yit9ql3e4ehITaMRAeyjgvNAsYbbdmDYVEBSGUK5zBTiQ9j9HF4JYDMX5vVZNNGKiH0lhYN1XkQEVeakTMrlxLSS_Ch4wTtHjWmwR21cF",
        #     ),
        #     load_page(browser, "https://www.eastmoney.com/"),
        #     load_page(
        #         browser,
        #         "https://pages.tmall.com/wow/z/import/tmg-rax-home/tmallimportHomewupr-index?wh_pid=tmg-website/index-pc&es=gjwaL/YjpozzX1yJ4zwwtm/89cPW8ghPFOPAbRUVwxn0EK3Y+YwXCwj83KfxNFDa&ali_trackid=2:mm_43125636_4246598_114660100071:1718876650_080_1073523900&union_lens=lensId:PUB@1671521062@2133dff0_0ad5_1852e6b4df9_c801@01@{%22floorId%22:38852,%22spmB%22:%22_portal_v2_pages_activity_official_index_htm%22};recoveryid:080_1823100399@1718876650712&pageId=20150318020009996&rootPageId=20150318020009996&bxsign=tbkuis079NVhX3iQvBtZiop3TwAp0204sTdOojNw_qvMs5mGOv-D1yuMJch61K5IXWapJeaQbirunHG--S2nU0usKb__qN4vFLKFr_50WKYFO0ZAwQTvo0nYZIXfgVblaTD9hJXDv1f27dHM44_BAMTbiCd0g46_pYBE569b8kM3GUxqxuZY8B0F2gLoO0PSz73",
        #     ),
        #     load_page(browser, "https://www.ctrip.com/?allianceid=1630&sid=40636345"),
        #     load_page(browser, "https://yiyan.baidu.com/?from=25"),
        #     load_page(browser, "https://www.ifeng.com/"),
        #     load_page(browser, "https://www.chsi.com.cn/"),
        #     load_page(browser, "https://www.douban.com/"),
        #     load_page(browser, "https://sh.58.com/?utm_source=market&spm=b-31580022738699-me-f-862.mingzhan"),
        #     load_page(browser, "https://baiduzm.37.com/?uid=3339810"),
        #     load_page(browser, "http://www.cpta.com.cn/"),
        #     load_page(browser, "https://basic.smartedu.cn/"),
        # ]
        tasks = [
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
            load_page(browser, "https://www.baidu.com"),
        ]
        start = DateTime.Now()
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=300)
        # for task in tasks:
        #     await task
        end = DateTime.Now()
        print("用时：" + str((end - start).TotalSecond) + "秒")
        # page = await browser.new_page()
        # await load_handler(page)
        # await page.goto(
        #     "https://www.gmanetwork.com/entertainment/showbizn`ews/news/113438/carla-abellana-attends-launch-of-bea-alonzos-new-line-of-travel-organizers/story",
        #     wait_until="commit",
        # )
        # await page.locator("//div[@class='content-details']").wait_for(timeout=30000, state="attached")
        # result = await page.content()
        # selector = ExSelector(result)
        # text_tags = selector.xpath(
        #     "//div[@class='content-details']//*[self::p|self::h1|self::h2|self::h3|self::h4|self::h5|self::h6|self::img]"
        # )
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
