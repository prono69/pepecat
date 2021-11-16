# Sedly made by t.me/i_osho | Idea by t.me/nvmded
import os
from random import choice

from userbot import catub

from ..core.managers import edit_delete
from . import reply_id

plugin_category = "fun"


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
        if reply.file.mime_type != "audio/mpeg":
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
