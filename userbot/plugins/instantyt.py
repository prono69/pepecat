#By Mine is Zarox (https://t.me/IrisZarox)
import asyncio
from datetime import datetime
from time import time

from . import hmention
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import catub
from ..helpers.utils import reply_id

plugin_category = "misc"

@catub.cat_cmd(
    pattern="iyt(?:\s|$)([\s\S]*)",
    command=("iyt", plugin_category),
    info={
        "header": "To download youtube video/shorts instantly",
        "examples": [
            "{tr}iyt <link>",
        ],
    },
)
async def _(zarox):
    "For downloading yt video/shorts instantly"
    chat = "@youtubednbot"
    reply_to_id = await reply_id(zarox)
    url = zarox.pattern_match.group(1)
    reply = await zarox.get_reply_message()
    if reply and url or not reply and url:
        mine = url
    elif reply and reply.raw_text:
        mine = reply.raw_text
    else:
        return await edit_delete(
            zarox, "__Provide youtube link along with cmd or reply to link"
        )
    if "youtu" not in mine:
        await edit_or_reply(
            zarox, "` I need a valid youtube link to download it's Video/Shorts...`"
        )
        return 
    else:
        start = datetime.now()
        catevent = await edit_or_reply(zarox, "**Downloading.....**")
    async with zarox.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(mine)
            await asyncio.sleep(0.5)
            video = await conv.get_response()
            await zarox.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**Error:** `unblock` @youtubednbot `and retry!`")
            return
        await catevent.delete()
        end = datetime.now()
        ms = (end - start).seconds
        if "short" in mine:
        	link = f"**➥Youtube short:**"
        else:
        	link = f"**➥Youtube video:**"
        caption = f"**➥ Video uploaded in {ms} seconds.**\n{link} [Link]({mine})"
        cat = await zarox.client.send_file(
            zarox.chat_id,
            video,
            caption=caption,
            reply_to=reply_to_id,
        )
    await zarox.client.delete_messages(
        conv.chat_id, [msg_start.id, response.id, msg.id, video.id,]
    )