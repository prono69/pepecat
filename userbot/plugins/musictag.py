# By https://t.me/feelded
import os
from telethon.tl.types import DocumentAttributeAudio
from ..helpers.utils import reply_id
from ..core.managers import edit_delete
from telethon import functions
from . import catub

plugin_category = "useless"

@catub.cat_cmd(
    pattern="cmt ?(.*)",
    command=("cmt", plugin_category),
    info={
        "header": "Changes musics tag",
        "examples": "{tr}cmt Loser : Neoni <reply>",
        "usage": [
            "{tr}cmt <song title>:<artist> <reply audio>",
        ],
    },
)
async def cmt(odi):
    "Musics tag"
    try:
        reply_to_id = await reply_id(odi)
        text = odi.pattern_match.group(1)
        reply = await odi.get_reply_message()
        if not (reply and reply.audio):
            await edit_delete(odi, "`Please reply an audio`")
        elif not (text and ":" in text):
            await edit_delete(odi, "`Try to do it with correct form`")
        else: #Under odi copyright :)
            await odi.edit("`Changing music tag...`")
            audio = await reply.download_media()
            x, y = text.replace(" ", "-").split(":")
            title = x.replace("-", " ")
            per = y.replace("-", " ")
            dur = reply.file.duration
            await odi.edit("`Uploading...`")
            await odi.client.send_file(odi.chat_id, audio, attributes=[DocumentAttributeAudio(title=title, performer=per, duration=dur)], reply_to=reply_to_id)
            await odi.delete()
            os.remove(audio)
    except Exception as e:
         await edit_delete(odi, f"**Error :**\n`{e}`", 7)
         os.remove(audio)
