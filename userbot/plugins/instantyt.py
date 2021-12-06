#created By Mine is Zarox (https://t.me/IrisZarox)
#thanx to @pony0boy for @youtubednbot

import asyncio
import requests
from time import time
from datetime import datetime

from . import hmention
from userbot import catub
from ..helpers.utils import reply_id
from ..helpers.functions import yt_search
from ..core.managers import edit_delete, edit_or_reply
from telethon.errors.rpcerrorlist import YouBlockedUserError

plugin_category = "misc"

def is_url(link):
    try:
        response = requests.get(link)
        url = "yes"
    except requests.exceptions.MissingSchema as exception:
        url = "no"
    return url

@catub.cat_cmd(
    pattern="(iyt)(a)?(?:\s|$)([\s\S]*)",
    command=("iyt", plugin_category),
    info={
        "header": "To download youtube video/shorts instantly",
        "examples": [
            "{tr}iyt <query/link/reply to link>",
        ],
        "note": "You can change the download settings here in @youtubednbot send /settings and proceed",
    },
)
async def _(zarox):
    "For downloading yt video/shorts instantly"
    chat = "@youtubednbot"
    reply_to_id = await reply_id(zarox)
    C = zarox.pattern_match.group(2)
    B = zarox.pattern_match.group(3)
    A = await zarox.get_reply_message()
    if A and A.message and not B:
        if "youtu" in A.message:
            mine = A.message
        else:
            return await edit_or_reply(zarox, "`I cant read minds giving something to search`")
    elif B:
        yt_str = is_url(B)
        if yt_str == "yes" and "youtu" in B:
            mine = B
        else:
            mine = await yt_search(str(B))
    else:
        return await edit_or_reply(zarox, "`I cant read minds give something to search`")
    await edit_or_reply(zarox, "**Downloading...**")
    async with zarox.client.conversation(chat) as conv:
        try:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                await zarox.client.send_read_acknowledge(conv.chat_id)
            except TimeoutError:
                return await edit_or_reply(zarox, "`Couldn't able to download the video. Try again later`")
            start = datetime.now()
            try:
                if C:
                    msg = await conv.send_message(f"/a {mine}", link_preview=True)
                else:
                    msg = await conv.send_message(mine, link_preview=True)
                await asyncio.sleep(0.1)
                video = await conv.get_response()
            except TimeoutError:
                await zarox.client.delete_messages(conv.chat_id, [msg.id])
                if C:
                    msg = await conv.send_message(f"/a {mine}", link_preview=True)
                else:
                    msg = await conv.send_message(mine, link_preview=True)
                await asyncio.sleep(0.1)
                video = await conv.get_response()
            await zarox.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(zarox, "**Error:** `unblock` @youtubednbot `and retry!`")
            return
        await zarox.delete()
        end = datetime.now()
        ms = (end - start).seconds
        try:
            caption = f"[{msg.media.webpage.title}]({mine})\n`➥In: {ms} seconds`"
        except:
            caption = ""
        cat = await zarox.client.send_file(
            zarox.chat_id,
            video,
            caption=caption,
            reply_to=reply_to_id,
        )
    await zarox.client.delete_messages(
        conv.chat_id, [msg_start.id, response.id, msg.id, video.id,]
    )