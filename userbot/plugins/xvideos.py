# Created by @kirito6969

"""xvideos, Get free Sax Videos"""

import bs4
import requests

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import age_verification
from ..helpers.utils import reply_id
from . import catub

plugin_category = "extra"


@catub.cat_cmd(
    pattern="xvdo ?(.*)",
    command=("xvdo", plugin_category),
    info={
        "header": "Generate direct download link from xvideos",
        "usage": "{tr}xvdo <xvideos link>",
    },
)
async def xvid(message):
    reply_to = await reply_id(message)
    if await age_verification(message, reply_to):
        return
    editer = await edit_or_reply(message, "`Please Wait.....`")
    msg = message.pattern_match.group(1)
    if not msg:
        await edit_delete(message, "`Enter xvideos url bish`")
        return
    try:
        req = requests.get(msg)
        soup = bs4.BeautifulSoup(req.content, "html.parser")

        soups = soup.find("div", {"id": "video-player-bg"})
        link = ""
        for a in soups.find_all("a", href=True):
            link = a["href"]
        await editer.edit(f"**HERE IS YOUR LINK 🌚**\n\n`{link}`")
    except Exception:
        await edit_delete(message, "**Something went wrong**")


@catub.cat_cmd(
    pattern="xsearch ?(.*)",
    command=("xsearch", plugin_category),
    info={
        "header": "Xvideo Searcher",
        "description": "Search sax videos from xvideos",
        "usage": "{tr}xsearch <search query>",
        "examples": "{tr}xsearch pure taboo",
    },
)
async def xvidsearch(message):
    await edit_or_reply(message, "`Please Wait.....`")
    reply_to = await reply_id(message)
    if await age_verification(message, reply_to):
        return
    msg = message.pattern_match.group(1)
    if not msg:
        await edit_delete(message, "`BTC! What i am supposed to search`")
        return
    try:
        qu = msg.replace(" ", "+")
        page = requests.get(f"https://www.xvideos.com/?k={qu}").content
        soup = bs4.BeautifulSoup(page, "html.parser")
        col = soup.findAll("div", {"class": "thumb"})

        links = ""

        for i in col:
            a = i.find("a")
            link = a.get("href")

            semd = link.split("/")[2]

            links += f"<a href='https://www.xvideos.com{link}'>• {semd.upper()}</a>\n"
        await edit_or_reply(
            message,
            f"<b>Search Query:</b> <code>{msg}</code>\n\n" + links,
            parse_mode="HTML",
            link_preview=False,
        )

    except Exception:
        await edit_delete(message, "**Something Went Wrong**")
