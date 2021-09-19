# Ported from Ultroid for pepecat by @kirito6969

import random
import re

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup as bs

from . import catub, edit_delete, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="devian ?(.*)",
    command=("devian", plugin_category),
    info={
        "header": "Devian-Art Image Search",
        "description": "It will search and send u the image from Devian art.",
        "usage": [
            "{tr}devian <search query> ; <no of pics>",
        ],
    },
)
async def downakd(e):
    match = e.pattern_match.group(1)
    if not match:
        return await edit_delete(e, "`Give Query to Search...`")
    Random = False
    if ";" in match:
        num = int(match.split(";")[1])
        if num == 1:
            Random = True
        match = match.split(";")[0]
    else:
        num = 5
    xd = await edit_or_reply(e, "`Processing...`")
    match = match.replace(" ", "+")
    link = "https://www.deviantart.com/search?q=" + match
    ct = requests.get(link).content
    st = bs(ct, "html.parser", from_encoding="utf-8")
    res = st.find_all("img", loading="lazy", src=re.compile("https://images-wixmp"))[
        :num
    ]
    if Random:
        res = [random.choice(res)]
    out = []
    num = 0
    for on in res:
        img = await download_file(on["src"], f"downloads/{match}-{num}.jpg")
        num += 1
        out.append(img)
    if len(out) == 0:
        return await xd.edit("`No Results Found!`")
    await e.client.send_file(
        e.chat_id, out, caption=f"Uploaded {len(res)} Images\n", album=True
    )
    await xd.delete()


async def download_file(link, name):
    """for files, without progress callback with aiohttp"""
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as re_ses:
            file = await aiofiles.open(name, "wb")
            await file.write(await re_ses.read())
            await file.close()
    return name
