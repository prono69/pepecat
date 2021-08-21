from userbot import catub

from . import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="now$",
    command=("now", plugin_category),
    info={
        "header": "Sends the song via @nowplaybot",
        "description": "Sends the currently listening song (on spotify) to Telegram. Authorize with @nowplaybot for the command to work.",
        "usage": "{tr}now",
    },
)
async def current(event):
    "Sends Muzik via @nowplaybot"
    reply_to_id = await reply_id(event)
    if event.fwd_from:
        return
    bot = "@nowplaybot"
    results = await event.client.inline_query(bot, "current link")
    await results[0].click(
        event.chat_id,
        reply_to=reply_to_id,
    )
    await event.delete()


# This is abandoned
""" 
@catub.cat_cmd(
    pattern="then$",
    command=("then", plugin_category),
    info={
        "header": "Sends previous playing song via @nowplaybot",
        "description": "Sends the last listening song (on spotify) to Telegram. Authorize with @nowplaybot for the command to work.",
        "usage": "{tr}now",
    },
)
async def current(event):
    "Exposes you by sending previous song played on spotify"
    reply_to_id = await reply_id(event)
    if event.fwd_from:
        return
    bot = "@nowplaybot"
    results = await event.client.inline_query(bot, "current")
    await results[1].click(event.chat_id, reply_to=reply_to_id,)
    await event.delete()
"""
