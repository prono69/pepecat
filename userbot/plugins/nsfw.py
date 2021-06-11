# By @kirito6969 for PepeBot
# Don't edit credits Madafaka
"""
This module can search images in danbooru and send in to the chat!

──「 **Danbooru Search** 」──
"""

import os
import urllib
from asyncio import sleep

import requests

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="ani(mu|nsfw) ?(.*)",
    command=("animu|aninsfw", plugin_category),
    info={
        "header": "Contains NSFW 🔞.\nTo search images in danbooru!",
        "usage": "{tr}animu <query>\n{tr}aninsfw <nsfw query>",
        "examples": "{tr}animu One punch man",
    },
)
async def danbooru(message):
    await edit_or_reply(message, "`Processing…`")

    rating = "Explicit" if "nsfw" in message.pattern_match.group(1) else "Safe"
    search_query = message.pattern_match.group(2)

    params = {
        "limit": 1,
        "random": "true",
        "tags": f"Rating:{rating} {search_query}".strip(),
    }

    with requests.get(
        "http://danbooru.donmai.us/posts.json", params=params
    ) as response:
        if response.status_code == 200:
            response = response.json()
        else:
            await edit_delete(
                message,
                f"`An error occurred, response code:` **{response.status_code}**",
                4,
            )
            return

    if not response:
        await edit_delete(message, f"`No results for query:` __{search_query}__", 4)
        return

    valid_urls = [
        response[0][url]
        for url in ["file_url", "large_file_url", "source"]
        if url in response[0].keys()
    ]

    if not valid_urls:
        await edit_delete(
            message, f"`Failed to find URLs for query:` __{search_query}__", 4
        )
        return
    for image_url in valid_urls:
        try:
            await message.client.send_file(message.chat_id, image_url)
            await message.delete()
            return
        except Exception as e:
            await edit_or_reply(message, f"{e}")
    await edit_delete(
        message, f"``Failed to fetch media for query:` __{search_query}__", 4
    )


@catub.cat_cmd(
    pattern="boobs(?: |$)(.*)",
    command=("boobs", plugin_category),
    info={
        "header": "NSFW 🔞\nYou know what it is, so do I !",
        "usage": "{tr}boobs",
        "examples": "{tr}boobs",
    },
)
async def boobs(e):
    a = await edit_or_reply(e, "`Finding some big boobs...`")
    await sleep(1)
    await a.edit("`Sending some big boobs...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename("*.jpg", "boobs.jpg")
    await e.client.send_file(e.chat_id, "boobs.jpg")
    os.remove("boobs.jpg")
    await a.delete()


@catub.cat_cmd(
    pattern="butts(?: |$)(.*)",
    command=("butts", plugin_category),
    info={
        "header": "NSFW 🔞\nBoys and some girls likes to Spank this 🍑",
        "usage": "{tr}butts",
        "examples": "{tr}butts",
    },
)
async def butts(e):
    a = await edit_or_reply(e, "`Finding some beautiful butts...`")
    await sleep(1)
    await a.edit("`Sending some beautiful butts...`")
    nsfw = requests.get("http://api.obutts.ru/butts/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename("*.jpg", "butts.jpg")
    await e.client.send_file(e.chat_id, "butts.jpg")
    os.remove("butts.jpg")
    await a.delete()


PENIS_TEMPLATE = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""


@catub.cat_cmd(
    pattern=r"(?:penis|dick)\s?(.)?",
    command=("dick | penis", plugin_category),
    info={
        "header": "NSFW 🔞\nThis is Something EPIC that horny girls wanna see for sure ! 🌚",
        "usage": "{tr}dick",
        "examples": "{tr}dick",
    },
)
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    o = await edit_or_reply(e, "`Dickifying...`")
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace("🍆", emoji)
    await o.edit(message)
