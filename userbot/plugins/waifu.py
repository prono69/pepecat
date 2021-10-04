# Imported from ppe-remix for PepeBot

import asyncio
import os
import random

from ..helpers.functions import deEmojify
from . import catub

plugin_category = "extra"
senpais = [37, 38, 48, 55]


@catub.cat_cmd(
    pattern="waifu(?: |$)(.*)",
    command=("waifu", plugin_category),
    info={
        "header": "Get waifu stickers",
        "description": "For custom waifu stickers",
        "usage": [
            "{tr}waifu <text>",
            "{tr}waifu <reply>",
        ],
        "examples": "{tr}waifu Oppai queen Rias",
    },
)
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("`No text given, hence the waifu ran away.`")
            return
    animus = [20, 32, 33, 37, 40, 41, 42, 58]
    sticcers = await animu.client.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await animu.edit(
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
        )
    await asyncio.sleep(3)
    await animu.delete()


@catub.cat_cmd(
    pattern="hz(:? |$)(.*)?",
    command=("hz", plugin_category),
    info={
        "header": "Hazmat Mask",
        "description": "Get hazmat mask ",
        "usage": [
            "{tr}hz <reply to a photo>",
            "{tr}hz <reply to a photo> [flip, x2, rotate (degree), background (number), black]",
        ],
    },
)
async def _(hazmat):
    await hazmat.edit("`Sending information...`")
    level = hazmat.pattern_match.group(2)
    if hazmat.fwd_from:
        return
    if not hazmat.reply_to_msg_id:
        await hazmat.edit("`WoWoWo Capt!, we are not going suit a ghost!...`")
        return
    reply_message = await hazmat.get_reply_message()
    if not reply_message.media:
        await hazmat.edit("`Word can destroy anything Capt!...`")
        return
    chat = "@hazmat_suit_bot"
    await hazmat.edit("```Suit Up Capt!, We are going to purge some virus...```")
    message_id_to_reply = hazmat.message.reply_to_msg_id
    msg_reply = None
    async with hazmat.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/hazmat {level}"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            elif reply_message.gif:
                m = "/hazmat"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            """ - don't spam notif - """
            await hazmat.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await hazmat.reply("`Please unblock` @hazmat_suit_bot`...`")
            return
        if response.text.startswith("I can't"):
            await hazmat.edit("`Can't handle this GIF...`")
            await hazmat.client.delete_messages(
                conv.chat_id, [msg.id, response.id, r.id, msg_reply.id]
            )
            return
        downloaded_file_name = await hazmat.client.download_media(
            response.media, Config.TMP_DOWNLOAD_DIRECTORY
        )
        await hazmat.client.send_file(
            hazmat.chat_id,
            downloaded_file_name,
            force_document=False,
            reply_to=message_id_to_reply,
        )
    await hazmat.delete()
    return os.remove(downloaded_file_name)


@catub.cat_cmd(
    pattern="senpai(?: |$)(.*)",
    command=("senpai", plugin_category),
    info={
        "header": "Get Senpai stickers!",
        "usage": [
            "{tr}senpai <text>",
            "{tr}senpai <reply>",
        ],
        "examples": "{tr}senpai Oppai Queen Rias",
    },
)
async def _(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer(
                "`No text given, hence the Senpai will beat u in the Toilet` 🌚"
            )
            return
    sticcers = await animu.client.inline_query(
        "stickerizerbot", f"#{random.choice(senpais)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await animu.edit(
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
        )
    await asyncio.sleep(4)
    await animu.delete()
