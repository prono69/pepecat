# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="wth ?(.*)",
    command=("wth",
    plugin_category),
      info={
        "header": "What the hell",
        "usage": "{tr}wth <username/reply>",
    },
)
async def anim(whatthehell):
    "What the hell"
    
    a = 1

    if a == 1 :
        wth = await edit_or_reply(whatthehell,"Uff 🤞🏻...")
        time.sleep(3)
        whati = await wth.edit(f"Uff ✌🏻...")
        time.sleep(9)
        await whati.edit(f"What the hell are you doing fucking idiot ? 👀")
    else:
      await edit_or_reply(f"Seems like something's wrong")
