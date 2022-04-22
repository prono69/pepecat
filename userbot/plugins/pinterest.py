# Created by @deepaiims

import asyncio
import os
import re

import requests

from userbot import catub

from ..core.managers import edit_or_reply
from . import mention

try:
    from pyquery import PyQuery as pq
except ModuleNotFoundError:
    os.system("pip3 install pyquery")
    from pyquery import PyQuery as pq

plugin_category = "extra"


def get_download_url(link):
    post_request = requests.post(
        "https://www.expertsphp.com/download.php", data={"url": link}
    )

    request_content = post_request.content
    str_request_content = str(request_content, "utf-8")
    download_url = pq(str_request_content)("table.table-condensed")("tbody")("td")(
        "a"
    ).attr("href")
    return download_url


@catub.cat_cmd(
    pattern="pint(?:\s|$)([\s\S]*)",
    command=("pint", plugin_category),
    info={
        "header": "To download pinterest posts",
        "options": "To download image and video posts from pinterest",
        "usage": [
            "{tr}pint <post link>",
        ],
    },
)
async def _(event):
    "To download pinterest posts"
    A = "".join(event.text.split(maxsplit=1)[1:])
    links = re.findall(r"\bhttps?://.*\.\S+", A)
    if not links:
        await edit_or_reply(event, "`Please give a valid link`")
        await asyncio.sleep(3)
        await event.delete()
    else:
        await edit_or_reply(event, "`Downloading...`")
        DEEP = get_download_url(A)
        await event.delete()
        await event.client.send_file(
            event.chat.id, DEEP, caption=f"➥ Uploaded by = {mention}\n➥ Pin = [Link]({A})"
        )
