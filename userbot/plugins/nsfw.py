# By @kirito6969 for PepeBot
# Don't edit credits Madafaka
"""
This module can search images in danbooru and send in to the chat!
──「 **Danbooru Search** 」──
"""

import os
import urllib

import requests

from userbot import catub

from ..helpers.functions import age_verification
from . import edit_delete, edit_or_reply, reply_id

plugin_category = "fun"


@catub.cat_cmd(
    pattern="ani(mu|nsfw) ?(.*)",
    command=("ani | animu | aninsfw", plugin_category),
    info={
        "header": "Contains NSFW 🔞.\nTo search images in danbooru!",
        "usage": [
            "{tr}animu <query>",
            "{tr}aninsfw <nsfw query>",
        ],
        "examples": [
            "{tr}animu naruto",
            "{tr}aninsfw boku no pico",
        ],
    },
)
async def danbooru(message):
    "Get anime charecter pic or nsfw"
    reply_to = await reply_id(message)
    if await age_verification(message, reply_to):
        return
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
            await message.client.send_file(
                message.chat_id, image_url, reply_to=reply_to
            )
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
    "Search boobs"
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    a = await edit_or_reply(e, "`Sending boobs...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve(f"http://media.oboobs.ru/{nsfw}", "*.jpg")
    os.rename("*.jpg", "boobs.jpg")
    await e.client.send_file(e.chat_id, "boobs.jpg", reply_to=reply_to)
    os.remove("boobs.jpg")
    await a.delete()


@catub.cat_cmd(
    pattern="butts(?: |$)(.*)",
    command=("butts", plugin_category),
    info={
        "header": "NSFW 🔞\nBoys and some girls are like to Spank this 🍑",
        "usage": "{tr}butts",
        "examples": "{tr}butts",
    },
)
async def butts(e):
    "Search beautiful butts"
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    a = await edit_or_reply(e, "`Sending beautiful butts...`")
    nsfw = requests.get("http://api.obutts.ru/butts/10/1/random").json()[0]["preview"]
    urllib.request.urlretrieve(f"http://media.obutts.ru/{nsfw}", "*.jpg")
    os.rename("*.jpg", "butts.jpg")
    await e.client.send_file(e.chat_id, "butts.jpg", reply_to=reply_to)
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
