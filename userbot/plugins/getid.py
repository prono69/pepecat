# Modified by @kirito6969

import html

from telethon.tl.types import User
from telethon.utils import get_display_name, pack_bot_file_id

from userbot import catub
from userbot.core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"

LOGS = logging.getLogger(__name__)


@catub.cat_cmd(
    pattern="(get_id|id)(?:\s|$)([\s\S]*)",
    command=("id", plugin_category),
    info={
        "header": "To get id of the group or user.",
        "description": "if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command",
        "usage": "{tr}id <reply/username>",
    },
)
async def _(event):
    "To get id of the group or user."
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"The id of the user `{input_str}` is `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"The id of the chat/channel `{p.title}` is `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "`Either give input as username or reply to user`")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**Current Chat ID : **`{event.chat_id}`\n**From User ID: **`{r_msg.sender_id}`\n**Media File ID: **`{bot_api_file_id}`",
            )

        else:
            await edit_or_reply(
                event,
                f"**Current Chat ID : **`{event.chat_id}`\n**From User ID: **`{r_msg.sender_id}`",
            )

    else:
        await edit_or_reply(event, f"**Current Chat ID : **`{event.chat_id}`")


@catub.cat_cmd(
    pattern="ids ?([\s\S]*)",
    command=("ids", plugin_category),
    info={
        "header": "To get id of the group or user.",
        "description": "If given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command",
        "usage": "{tr}ids <reply/username>",
    },
)
async def get_id(e):
    custom = e.pattern_match.group(1)
    if custom:
        try:
            custom = int(custom)
        except ValueError:
            pass
        try:
            en = await e.client.get_entity(custom)
        except ValueError:
            await edit_delete(e, "**Err** \\\nUnknown entity")
            return
        id = await e.client.get_peer_id(en)
        text = html.escape(get_display_name(en))
        if isinstance(en, User):
            text = f'<a href="tg://user?id={id}">{text}</a>'
        elif getattr(en, "username", None):
            text = f'<a href="tg://resolve?domain={en.username}">{text}</a>'
        text += f"'s ID: <code>{id}</code>"
        await edit_or_reply(e, text, parse_mode="HTML")
        return
    text = f"<b>👥 Chat ID:</b> <code>{e.chat_id}</code>\n"
    text += f"<b>💬 Message ID:</b> <code>{e.id}</code>\n"
    text += f'<b>🙋‍♂️ Your ID:</b> <code>{e.sender_id}</code> • <a href="tg://user?id={e.sender_id}">Link</a>\n'
    if e.is_reply:
        text += "\n"
        r = await e.get_reply_message()
        text += f"<b>RepliedMessage ID:</b> <code>{r.id}</code>\n"
        text += f'<b>RepliedSender ID:</b> <code>{r.sender_id}</code> • <a href="tg://user?id={r.sender_id}">Link</a>\n'
        if getattr(r.fwd_from, "from_id", None):
            text += f'<b>RepliedForward SenderID:</b> <code>-100{r.fwd_from.from_id.channel_id}</code> • <a href="tg://user?id=-100{r.fwd_from.from_id.channel_id}">Link</a>\n'
    await edit_or_reply(e, text, parse_mode="HTML")
