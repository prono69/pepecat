# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="shit ?(.*)",
    command=("shit",
    plugin_category),
      info={
        "header": "Shit",
        "usage": "{tr}shit <username/reply>",
    },
)
async def anim(shit):
    "Shit"
    
    a = 1

    if a == 1 :
        sh = await edit_or_reply(shit,"Err 🤞🏻...")
        time.sleep(3)
        shiti = await sh.edit(f"Err ✌🏻...")
        time.sleep(9)
        await shiti.edit(f"You're fucking piece of shit 🙄")
    else:
      await edit_or_reply(f"Seems like something's wrong")
