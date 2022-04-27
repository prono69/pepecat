# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="bloody ?(.*)",
    command=("bloody",
    plugin_category),
      info={
        "header": "Bloody",
        "usage": "{tr}bloody <username/reply>",
    },
)
async def anim(hell):
    "Bloody"
    
    a = 1

    if a == 1 :
        bh = await edit_or_reply(hell,"Esh 🤞🏻...")
        time.sleep(3)
        helli = await bh.edit(f"Esh ✌🏻...")
        time.sleep(9)
        await helli.edit(f"Huh you bloody hell 😑/n/nGo to hell")
    else:
      await edit_or_reply(f"Seems like something's wrong")
