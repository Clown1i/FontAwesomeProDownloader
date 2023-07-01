"""
自动下载Font-Awesome-Pro的字体文件和CSS文件
注意，Pro本身需要付费，喜欢的话还请去支持正版
https://fontawesome.com/
"""
import aiohttp
import re
import os
import asyncio

# 下载路径
VERSION = '6.4.0'
PATH = "https://site-assets.fontawesome.com/releases/v" + VERSION
# 下载异步任务数量
TASK_NUMBER = 100


async def main():
    if not os.path.exists("/css/all.css"):
        if not os.path.exists("./css"):
            os.mkdir("./css")
        # 下载CSS文件
        print("CSS文件不存在，正在下载")
        async with aiohttp.ClientSession() as session:
            await downloader(["/css/all.css"], session)

    # 分析CSS文件
    with open("./css/all.css") as f:
        css = f.read()

    if not os.path.exists("./webfonts"):
        os.mkdir("./webfonts")

    pattern = re.compile("url\(\.\.(/webfonts/.*?)\)")
    results = re.findall(pattern, css)

    def filter_(value):
        if value.endswith("eot") or value.endswith("woff") or value.endswith("woff2"):
            return True
        return False
    # 删除多余URL
    results = list(filter(filter_, results))
    # 去重
    results = list(set(results))
    # 分配任务
    length = len(results)
    print("共需要下载：", length, "个文件")
    task_missions = []
    for i in range(TASK_NUMBER):
        task_missions.append([])
    needle = 0
    while len(results) > 0:
        task_mission = results.pop()
        task_missions[needle].append(task_mission)
        needle += 1
        if needle >= TASK_NUMBER:
            needle = 0
    async with aiohttp.ClientSession() as session:
        furthers = []
        for mission in task_missions:
            further = downloader(mission, session)
            furthers.append(further)
        await asyncio.gather(*furthers)


async def downloader(urls, session):
    for url in urls:
        async with session.get(PATH + url) as resp:
            resp.raise_for_status()
            save_path = "." + url
            with open(save_path, "wb") as f:

                f.write(await resp.read())
                print("保存成功", url)


if __name__ == '__main__':
    asyncio.run(main())
