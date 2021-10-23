import asyncio
import os
import random
from datetime import datetime

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus
from . import catub, hmention, mention, reply_id

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
    start = datetime.now()
    catevent = await edit_or_reply(event, f"`Checking`")
    end = datetime.now()
    ms = str((end - start).microseconds / 1000)
    for normal in ms:
        if normal in normaltext:
            pingchars = pingfont[normaltext.index(normal)]
            ms = ms.replace(normal, pingchars)
    my = f"𝗣𝗶𝗻𝗴:\n`{ms}` 𝗺𝘀"
    ping_caption = gvarstatus("PING_TEMPLATE") or my
    if flag == " -a":
        catevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await catevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await catevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = str(round((tms - 0.6) / 3, 3))
        for normal in ms:
            if normal in normaltext:
                pingchars = pingfont[normaltext.index(normal)]
                ms = ms.replace(normal, pingchars)
        await catevent.edit(
            f"<b> 𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗣𝗼𝗻𝗴!<b>\n <code>{ms} 𝗺𝘀<code>",
            parse_mode="html",
        )
    else:
        ping_caption = gvarstatus("PING_TEMPLATE") or my
        caption = ping_caption.format(ping=ms, mention=mention)
        await catevent.edit(caption)


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
        gvarstatus("PING_PICS")
        or "https://telegra.ph/file/1328d62db93ad22b69ba2.jpg https://telegra.ph/file/b2da6e4c55dd29600e4ed.jpg"
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
