# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

import aiohttp
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, catub, catversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"
sucks = "The stars sure are beautiful tonight | Am I frightening... woman? "  # dis is str for a reason


async def get_anime_quote():
    url = "https://waifu.it/api/v4/quote"
    headers = {"Authorization": "NDE0OTk4MTA0MzQyMDAzNzIz.MTcxODQyNDM5NA--.ab7207fceb"}

    timeout = aiohttp.ClientTimeout(total=8)

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, headers=headers) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()
                return data
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return None


@catub.cat_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "Check bot alive status",
        "options": "Set ALIVE_PIC with media link (use .tgm)",
        "usage": ["{tr}alive"],
    },
)
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    catevent = await edit_or_reply(event, "`Checking...`")

    start = datetime.now()

    # Uptime & ping
    uptime = await get_readable_time(time.time() - StartTime)
    ping = (datetime.now() - start).microseconds / 1000

    # DB health
    _, db_health = check_data_base_heal_th()

    # Vars
    EMOJI = gvarstatus("ALIVE_EMOJI") or "〣 "
    CAT_IMG = gvarstatus("ALIVE_PIC")
    cat_caption = gvarstatus("ALIVE_TEMPLATE") or temp

    ANIME = None
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or sucks

    # Fetch anime quote (safe)
    quote_data = await get_anime_quote()

    if quote_data:
        quote = quote_data.get("quote", "")
        author = quote_data.get("author", "")
        anime = quote_data.get("anime", "")

        if len(quote) <= 150:
            ALIVE_TEXT = f"__{quote}__"
            ANIME = f"**“{quote}” - {author} ({anime})**"

    # Final caption
    caption = cat_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME or "",
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=db_health,
        ping=ping,
    )

    # Send media or text
    try:
        if CAT_IMG:
            pics = CAT_IMG.split()
            pic = random.choice(pics)
            await event.client.send_file(
                event.chat_id,
                pic,
                caption=caption,
                reply_to=reply_to_id,
            )
            await catevent.delete()
        else:
            await edit_or_reply(catevent, caption)

    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        await edit_or_reply(
            catevent,
            "**Media Error!**\nUse `.setdv` to update ALIVE_PIC.",
        )


temp = """**{ALIVE_TEXT}**

**{EMOJI} Sensi :** {mention}
**{EMOJI} Database :** `{dbhealth}`
**{EMOJI} Uptime :** `{uptime}`
**{EMOJI} Telethon Version :** `{telever}`
**{EMOJI} Catuserbot Version :** `{catver}`
**{EMOJI} Python Version :** `{pyver}`"""


def catalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    cat_caption = "**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    return cat_caption


@catub.cat_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}ialive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, "ialive")
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
