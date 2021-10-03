# By @P_4_PEEYUSH
# Heavily Modified and fixed By @kirito6969 for pepecat

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import catub, eod, eor, reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="xxshort",
    command=("xxshort", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}xxshort",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    chat = "@OpGufaBot"
    k = await eor(event, "`Checking...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("🤪")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @OpGufaBot```")
            return


@catub.cat_cmd(
    pattern="xxlong",
    command=("xxlong", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}xxlong",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    k = await eor(event, "`Checking...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("😏")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @OpGufaBot```")
            return


@catub.cat_cmd(
    pattern="xpic",
    command=("xpic", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}xpic",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    k = await eor(event, "```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("💋")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @OpGufaBot```")
            return


@catub.cat_cmd(
    pattern="xnxx",
    command=("xnxx", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}xnxx",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    chat = "@SeXn1bot"
    k = await eor(event, "```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("💋2016 Videolar🔞")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @SeXn1bot```")
            return


@catub.cat_cmd(
    pattern="picx",
    command=("picx", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}picx",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    chat = "@SeXn1bot"
    k = await eor(event, "```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("♨️Old photo👙")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @SeXn1bot```")
            return


@catub.cat_cmd(
    pattern="les",
    command=("les", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}les",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    chat = "@SeXn1bot"
    k = await eor(event, "```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("🔞Uz_sex♨️")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @SeXn1bot```")
            return


@catub.cat_cmd(
    pattern="lis",
    command=("lis", plugin_category),
    info={
        "header": "NSFW",
        "description": "Try Yourself!",
        "usage": "{tr}lis",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    chat = "@SeXn1bot"
    k = await eor(event, "```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("🔞SeX_Vido🚷")
            response = await conv.get_response()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id
            )
            await k.delete()
        except YouBlockedUserError:
            await eod(event, "```Unblock @SeXn1bot```")
            return
