#By @deepaiims
from ..helpers.utils import reply_id
from telethon.errors.rpcerrorlist import YouBlockedUserError
from ..core.managers import edit_delete, edit_or_reply
from telethon import Button, functions
from ..helpers.utils import _format
from . import catub, hmention

plugin_category = "extra"

@catub.cat_cmd(
    pattern="fsong ?(.*)",
    command=("fsong", plugin_category),
    info={
        "header": "Song downloader",
        "examples": "{tr}fsong humdard",
        "usage": [
            "{tr}fsong <song name>",
        ],
    },
)
async def wave(deep):
    "Song dl by @deepaiims"
    song = "".join(deep.text.split(maxsplit=1)[1:])
    reply_to_id = await reply_id(deep)
    await deep.edit("`Downloading....`")
    if not song:
        await edit_delete(deep, "`Give me a song name`")
    chat = "@WaveyMusicBot"
    async with deep.client.conversation(chat) as conv:
        try:
            await deep.client(functions.contacts.UnblockRequest(conv.chat_id))
            s = await conv.send_message('/start')
            await conv.get_response()
            e = await conv.send_message(song)
            message = await conv.get_response()
            await deep.client.send_file(deep.chat_id, message, reply_to=reply_to_id, caption=False)
            await deep.delete()
            msgs = []
            for _ in range(s.id, e.id+2): msgs.append(_)
            await deep.client.delete_messages(conv.chat_id, msgs)
            await deep.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_delete(deep, "`Something went wrong`")
