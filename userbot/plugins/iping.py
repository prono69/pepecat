# Inline ping by @yuki
import re
from datetime import datetime

from telethon.events import CallbackQuery

from ..Config import Config
from . import BOTLOG_CHATID, catub, reply_id

plugin_category = "tools"


@catub.cat_cmd(
    pattern="iping$",
    command=("iping", plugin_category),
    info={
        "header": "Shows bot ping in inline mode",
        "options": "Bruh , why do this exists",
        "usage": [
            "{tr}iping",
        ],
    },
)
async def edit_and_u_gay(deep):
    "Inline ping"
    reply_to_id = await reply_id(deep)
    results = await deep.client.inline_query(Config.TG_BOT_USERNAME, "ping")
    await results[0].click(deep.chat_id, reply_to=reply_to_id, hide_via=True)
    await deep.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"ping")))
async def ping(event):
    start = datetime.now()
    life = await event.client.send_message(BOTLOG_CHATID, "Just for ping")
    await life.delete()
    end = datetime.now()
    ms = str((end - start).microseconds / 1000)
    ping_data = f" ꧁𝐏𝐢𝐧𝐠꧂ {ms}ms"
    await event.answer(ping_data, cache_time=0, alert=True)
