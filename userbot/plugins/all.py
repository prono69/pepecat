# Made by t.me/i_osho
import asyncio
from random import choice

from telethon.tl.functions.channels import GetFullChannelRequest

from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

msg = []
emoji = [
    "😀",
    "😬",
    "😱",
    "😱",
    "😦",
    "😃",
    "😖",
    "🤩",
    "😢",
    "😱",
    "😲",
    "🤮",
    "🤪",
    "🤨",
    "🤥",
    "🤠",
    "🦕",
    "🤡",
    "👊",
    "🤝",
    "😬",
    "🤷",
    "🎅",
    "🤪",
    "👩",
    "‍👩",
    "‍👧",
    "‍👧",
    "😖",
    "🤶",
    "👮",
    "👦",
    "🧓",
    "👢",
    "🧙",
    "🧞",
    "‍♀️",
    "🧛",
    " ♂️",
    "🐓",
    "🦀",
    "🦁",
    "🐋",
    "🐕",
    "🦊",
    "🐲",
    "🐅",
    "🐃",
    "🐓",
    "🦏",
    "🐿",
    "🦃",
    "🦓",
    "🌷",
    "🌾",
    "🎄",
    "🌒",
    "🌞",
    "🌙",
    "🌥",
    "🚒",
    "🌰",
    "🍇",
    "🥐",
    "🍟",
    "🥡",
    "🍘",
    "🍕",
    "🎱",
    "🥊",
    "🚶",
    "‍♀️",
    "🤼",
    "‍♂️",
    "🏑",
    "🎼",
    "🎷",
    "🚕",
    "🚌",
    "🛣",
    "🚉",
    "🚒",
    "🌠",
    "🌅",
    "🎠",
    "🏪",
    "🕌",
    "🏢",
    "🏯",
    "📽",
    "📱",
    "🕳",
    "✂",
    "☪",
    "♒",
    "☢",
    "♏",
    "📗",
]


@catub.cat_cmd(
    pattern="sure ?(.*)",
    command=("sure", "extra"),
    info={
        "header": "Tags ALL, literally all members in a group",
        "description": "By default tags 100 user/msg\nSee example if you want lesser users/msg",
        "usage": ["{tr}sure", "{tr}sure 1-100", "{tr}sure 25"],
    },
)
async def current(event):
    "Fking overkill tagall"
    if event.fwd_from:
        return
    if event.sender.id != 986755683:
        await edit_delete(event, "`Currently you can't use this :)`", 30)
        return
    reply_to_id = await reply_id(event)
    await event.get_reply_message()
    chat_ = await event.client.get_entity(event.chat.id)
    chat_info_ = await event.client(GetFullChannelRequest(channel=chat_))
    members = chat_info_.full_chat.participants_count

    input_ = event.pattern_match.group(1)
    if input_:
        if input_.isalpha():
            await edit_delete(event, "`Braaah`", 15)
            return
        if int(input_) > 100:
            await edit_delete(event, "`You can't tag more than 100 user/msg`", 15)
            return
        if int(input_) <= 0:
            await edit_delete(event, "`BRAH!! seriously`", 15)
            return
        else:
            permsg = int(input_)
    else:
        permsg = 100
    if members % permsg != 0:
        extra = True
    else:
        extra = False
    tagged = 0
    await event.delete()

    async for user in event.client.iter_participants(event.chat.id, limit=members):
        is_bot = user.bot
        if not is_bot:
            msg.append((f"<a href = tg://user?id={user.id}>⁪⁬⁮⁮⁮⁮</a>"))
            tagged += 1
            if extra:
                if tagged == members % permsg:
                    send = "⁪⁬⁮⁮⁮⁮".join(msg)
                    await event.client.send_message(
                        event.chat.id,
                        f"{choice(emoji)} {send}",
                        reply_to=reply_to_id,
                        parse_mode="html",
                    )
                    await asyncio.sleep(0.5)
                    msg.clear()
                    tagged = 0
                    extra = False
            elif tagged == permsg:
                send = "⁪⁬⁮⁮⁮⁮".join(msg)
                await event.client.send_message(
                    event.chat.id,
                    f"{choice(emoji)} {send}",
                    reply_to=reply_to_id,
                    parse_mode="html",
                )
                await asyncio.sleep(0.5)
                msg.clear()
                tagged = 0
