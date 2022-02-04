# By Yato.. https://t.me/nvmded

import os
from random import choice

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="dis$",
    command=("dis", plugin_category),
    info={
        "header": "To distort the replied media",
        "usage": [
            "{tr}dis <in reply to a media>",
        ],
    },
)
async def _(event):
    "To distort media"
    chat = event.chat_id
    reply_to_id = await reply_id(event)
    ded = await event.get_reply_message()
    mediatype = media_type(ded)
    try:
        if (
            mediatype not in ["Gif", "Sticker", "Photo", "Video"]
            or ded.file.mime_type == "application/x-tgsticker"
        ):
            await edit_or_reply(event, "` I need a proper media to distort it`")
            return
        else:
            await edit_or_reply(
                event,
                "` Distorting...`",
            )
    except:
        pass
    bot = "@distortionerbot"
    async with event.client.conversation(bot, exclusive=False) as conv:  #
        try:
            start = await conv.send_message(ded)
            end = await conv.get_response()
            if media_type(end) in ["Sticker", "Photo"]:
                to_send = end
                pepecat = await event.client.send_file(
                    chat, file=to_send, reply_to=reply_to_id
                )
                await event.delete()
                await start.delete()
                await end.delete()
            else:
                end2 = await conv.get_response()
                to_send = end2
                pepecat = await event.client.send_file(
                    chat, file=to_send, reply_to=reply_to_id
                )
                await event.delete()
                await start.delete()
                await end.delete()
                await end2.delete()
            out = media_type(end2)
            if out in ["Gif", "Video", "Sticker"]:
                await _catutils.unsavegif(event, pepecat)
        except YouBlockedUserError:
            await edit_delete(
                event, "**Error:**\nUnblock @distortionerbot and try again"
            )


@catub.cat_cmd(
    pattern="daudio( -r|$)",
    command=("daudio", plugin_category),
    info={
        "header": "Distorts the replied audio file.",
        "flags": {
            "r": "Use flag `-r` for ear rape version",
        },
        "usage": ["{tr}daudio", "{tr}daudio -r"],
    },
)
async def kill_mp3(event):
    "Distorts audio files"
    flag = event.pattern_match.group(1)
    pawer = choice(range(10, 21))
    reply = await event.get_reply_message()
    reply_to_id = await reply_id(event)
    try:
        type_ = reply.file.mime_type
        if "audio" not in type_:
            await edit_delete(event, "`Reply to a audio file brah!!`")
    except:
        await edit_delete(event, "`Reply to a audio file brah!!`")

    await event.edit("`Downloading...`")
    if not os.path.isdir("destiny"):
        os.makedirs("destiny")
    else:
        os.system("rm -rf destiny")
        os.makedir("destiny")
    file = await reply.download_media("destiny/sed.mp3")
    ded_file = "destiny/ded-sed.mp3"
    if flag == " -r":
        os.system(
            f'ffmpeg -i {file} -af "superequalizer=1b=20:2b=20:3b=20:4b=20:5b=20:6b=20:7b=20:8b=20:9b=20:10b=20:11b=20:12b=20:13b=20:14b=20:15b=20:16b=20:17b=20:18b=20,volume=5" {ded_file}'
        )
    else:
        os.system(f'ffmpeg -i {file} -filter_complex "vibrato=f={pawer}" {ded_file}')
    await event.edit("`Conversion done! Uploading audio.`")
    await event.client.send_file(
        event.chat_id,
        file=ded_file,
        caption=f"**| Successfully Destroyed |**",
        reply_to=reply_to_id,
    )
    await event.delete()
    os.system("rm -rf destiny")
