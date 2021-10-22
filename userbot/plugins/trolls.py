# credits to @mrconfused and @sandy1709
#    Copyright (C) 2020  sandeep.n(π.$)

import os

from telegraph import exceptions, upload_file

from userbot import catub

from ..core.managers import edit_or_reply
from ..helpers.utils import _cattools, get_user_from_event, reply_id
from . import convert_toimage, deEmojify, phcomment, threats, trap, trash

plugin_category = "fun"


async def purge():
    try:
        os.system("rm *.png *.webp")
    except OSError:
        pass


@catub.cat_cmd(
    pattern="trash$",
    command=("trash", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}trash",
    },
)
async def catbot(event):
    "image meme creator."
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "reply to a supported media file")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await event.reply(file=download_location)
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await trash(cat)
    os.remove(download_location)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@catub.cat_cmd(
    pattern="threat$",
    command=("threat", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}threats",
    },
)
async def catbot(event):
    "image meme creator."
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "reply to a supported media file")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await threats(cat)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@catub.cat_cmd(
    pattern="trap(?:\s|$)([\s\S]*)",
    command=("trap", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "Description": "creates a trap card",
        "usage": "{tr}trap (name of the person to trap) ; (trapper name)",
    },
)
async def catbot(event):
    "image meme creator."
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        text1, text2 = input_str.split(";")
    else:
        return await edit_or_reply(
            event,
            "**Syntax :** reply to image or sticker with `.trap (name of the person to trap);(trapper name)`",
        )
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "reply to a supported media file")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await trap(text1, text2, cat)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@catub.cat_cmd(
    pattern="phub(?:\s|$)([\s\S]*)",
    command=("phub", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "description": "pornhub comment creator",
        "usage": "{tr}phub <reply> <message>",
    },
)
async def phcomment(event):
    "Punhab comment maker"
    try:
        await edit_or_reply(event, "`Processing..`")
        text = event.pattern_match.group(1)
        reply = await event.get_reply_message()
        reply_to = await reply_id(event)
        if reply:
            user = await get_user_from_event(event)
            if user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.first_name
            text = text if text else str(reply.message)
        elif text:
            user = await catub.get_me()
            if user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.first_name
            text = text
        else:
            return await edit_delete(event, "`Give text bitch`")
        try:
            photo = await event.client.download_profile_photo(
                user.id,
                str(user.id) + ".png",
                download_big=False,
            )
            uplded = upload_image(photo)
        except BaseException:
            uplded = "https://telegra.ph/file/7d110cd944d54f72bcc84.jpg"
    except BaseException as e:
        await purge()
        return await edit_delete(event, f"`Error: {e}`")
    img = await phcomment(uplded, text, name)
    try:
        await event.client.send_file(
            event.chat_id,
            img,
            reply_to=reply_to,
        )
    except BaseException:
        await purge()
        return await edit_delete(event, "`Reply message has no text!`")
    await event.delete()
    await purge()
