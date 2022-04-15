from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "utils"


@catub.cat_cmd(
    pattern="ctg$",
    command=("ctg", plugin_category),
    info={
        "header": "Reply to link To get link preview using telegrahs",
        "usage": "{tr}ctg",
    },
)
async def _(event):
    "To get link preview"
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "```Reply to a link```")
        return
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to a link```")
        return
    chat = "@chotamreaderbot"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "`RIP Check your blacklist boss and unblock @chotamreaderbot`"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("Am I dumb or am I dumb ?")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
