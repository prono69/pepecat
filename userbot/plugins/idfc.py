# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="idfc ?(.*)",
    command=("idfc",
    plugin_category),
      info={
        "header": "I don't fucking care",
        "usage": "{tr}idfc <username/reply>",
    },
)
async def anim(fucking):
    "I don't fucking care"
    
    a = 1

    if a == 1 :
        idfc = await edit_or_reply(fucking, "Err 🤞🏻...")
        time.sleep(3)
        fucki = await idfc.edit(f"Err ✌🏻...")
        time.sleep(9)
        await fucki.edit(f"I don't fucking care 🥰")
    else:
      await edit_or_reply(f"Seems like something's wrong")
