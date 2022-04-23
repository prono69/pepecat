import asyncio
import os
import random
import re
import time
from datetime import datetime

import requests
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import get_readable_time
from ..sql_helper.globals import gvarstatus
from . import BOTLOG_CHATID, StartTime, catub, hmention, mention, reply_id

plugin_category = "tools"

# =========Some integrated custom vars============

normaltext = "1234567890."
pingfont = [
    "𝟭",
    "𝟮",
    "𝟯",
    "𝟰",
    "𝟱",
    "𝟲",
    "𝟳",
    "𝟴",
    "𝟵",
    "𝟬",
    "•",
]

# Pre text i.e. before calculation ping
PING_TEXT = os.environ.get("PING_TEXT") or "𝔖𝔱𝔞𝔯𝔱𝔦𝔫𝔤 𝔗𝔥𝔢 𝔊𝔞𝔪𝔢!!"
# Post text i.e. the final message
PONG_TEXT = os.environ.get("PONG_TEXT") or "𝔑𝔬𝔴, 𝔏𝔢𝔱 𝔗𝔥𝔢 𝔊𝔞𝔪𝔢 𝔅𝔢𝔤𝔦𝔫!!"
# Custom mention line
PING_MENTION = os.environ.get("PING_MENTION") or "ℜ𝔲𝔩𝔢𝔰 𝔅𝔶"
# lol
PONG = "ɪ ꜱʟᴀʏ ᴅʀᴀɢᴏɴꜱ ᴀᴛ ɴɪɢʜᴛ ᴡʜɪʟᴇ ʏᴏᴜ ꜱʟᴇᴇᴘ🖤🥀"

temp_ = "Pong!"
temp = "Pong!\n`{ping} ms`"
if Config.BADCAT:
    temp_ = "__**☞ Pong**__"
    temp = "__**☞ Pong**__\n➥ `{ping}` **ms**\n➥ __**Bot of **__{mention}"


@catub.cat_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    # my = f"𝗣𝗶𝗻𝗴:\n`{ms}` 𝗺𝘀"
    if flag == " -a":
        catevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await edit_or_reply(catevent, "`..!..`")
        await asyncio.sleep(0.3)
        await edit_or_reply(catevent, "`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        for normal in ms:
            if normal in normaltext:
                pingchars = pingfont[normaltext.index(normal)]
                ms = ms.replace(normal, pingchars)
        await edit_or_reply(catevent, f"**𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗣𝗼𝗻𝗴!**\n`{ms} 𝗺𝘀`")
    else:
        catevent = await edit_or_reply(event, temp_)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        ANIME = None
        ping_temp = gvarstatus("PING_TEMPLATE") or temp
        PING_PIC = gvarstatus("PING_PIC")
        if "ANIME" in ping_temp:
            data = requests.get("https://animechan.vercel.app/api/random").json()
            ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
        caption = ping_temp.format(
            ANIME=ANIME,
            mention=mention,
            uptime=uptime,
            ping=ms,
        )
        if PING_PIC:
            CAT = list(PING_PIC.split())
            PIC = random.choice(CAT)
            try:
                await event.client.send_file(
                    event.chat_id, PIC, caption=caption, reply_to=reply_to_id
                )
                await catevent.delete()
            except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
                return await edit_or_reply(
                    catevent,
                    f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
                )
        else:
            await edit_or_reply(
                catevent,
                caption,
            )


@catub.cat_cmd(
    pattern="mping$",
    command=("mping", plugin_category),
    info={
        "header": "Checks the latency of userbot from the server, with a media",
        "option": "VARS to customize the texts of mping\n`PING_PICS` add mutiple telegraph media link separated by spaces.\n`PING_TEXT` Pre text i.e. before calculation ping.\n`PONG_TEXT` Post text i.e. the final message.\n`PING_MENTION` Custom mention line.\n`PING_PARTNER` Text after ping(that random number)\n`AVG_TEXT Custom header in `.ping -a``",
        "usage": "{tr}mping",
    },
)
async def _(event):
    "Shows ping with a given random media"
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    PING_PICS = (
        gvarstatus("PING_PIC")
        or "https://telegra.ph/file/1328d62db93ad22b69ba2.jpg, https://telegra.ph/file/b2da6e4c55dd29600e4ed.jpg"
    )
    PING_PICS = PING_PICS.rsplit(",")
    start = datetime.now()
    cat = await edit_or_reply(event, "<b><i>Ｓｌａｙｉｎｇ　🥀　</b></i>", parse_mode="html")
    end = datetime.now()
    await cat.delete()
    ms = str((end - start).microseconds / 1000)
    PING_PIC = random.choice(PING_PICS)
    if PING_PIC:
        try:
            while PING_PIC == "":
                PING_PIC = random.choice(PING_PICS)
        except IndexError:
            error = "fix"  # This line is just to prevent any NoneType error
        caption = f"<b><i>{PONG}<i><b>\n<code>✦ {ms} ms</code>\n✦ <b><i>Ｓｅｎｓｅｉ　タくエ－　{hmention}</b></i>"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )


# Inline Ping by t.me/i_osho


@catub.cat_cmd(
    pattern="iping$",
    command=("iping", plugin_category),
    info={
        "header": "Checks bot ping via inline mode",
        "usage": [
            "{tr}iping",
        ],
    },
)
async def edit_and_u_gay(osho):
    "Inline Ping"
    reply_to_id = await reply_id(osho)
    results = await osho.client.inline_query(Config.TG_BOT_USERNAME, "ping")
    await results[0].click(osho.chat_id, reply_to=reply_to_id, hide_via=True)
    await osho.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"ping")))
async def ping(event):
    start = datetime.now()
    life = await event.client.send_message(BOTLOG_CHATID, "Just For Ping")
    await life.delete()
    end = datetime.now()
    ms = str((end - start).microseconds / 1000)
    ping_data = f"「 𝗣𝗶𝗻𝗴 」 {ms}ms"
    await event.answer(ping_data, cache_time=0, alert=True)
