# Modified by @kirito6969 for pepecat
# Very Dangerous Plugin!


import os
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from . import catub, eor, eod

plugin_category = "extra"

@catub.cat_cmd(
    pattern="gcast ?(.*)",
    command=("gcast", plugin_category),
    info={
        "header": "USE AT YOUR OWN RISK!\nSend message to all groups at once!",
        "usage": "{tr}gcast <input>",
        "examples": "{tr}gcast Hello World",
    },
)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return eod(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await eor(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")


@catub.cat_cmd(
    pattern="pcast ?(.*)",
    command=("pcast", plugin_category),
    info={
        "header": "ACCOUNT MAY GET BANNED\nSend message to all dm's at once!",
        "usage": "{tr}pcast <input>",
        "examples": "{tr}pcast Hello World!",
    },
)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return eod(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    kk = await eor(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")
