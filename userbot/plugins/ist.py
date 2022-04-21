#By @yuki
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@catub.cat_cmd(
    pattern="ist ?(.*)",
    command=("ist", plugin_category),
    info={
        "header": "Inline write-on sticker",
        "usage": [
            "{tr}ist <your text>",
        ],
    },
)
async def isong(event):
    if event.fwd_from: 
        return
    bot = "QuotAfBot"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not text:
        await edit_delete(event, "`Give me a text`")
    else:
        await event.delete()
        run = await event.client.inline_query(bot, text)
        result = await run[1].click("me")
        await event.client.send_message(event.chat_id, result, reply_to=reply_to_id)
        await result.delete()
