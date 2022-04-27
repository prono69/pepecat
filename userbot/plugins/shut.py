# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="shut up ?(.*)",
    command=("shut up",
    plugin_category),
      info={
        "header": "Shut up",
        "usage": "{tr}shut <username/reply>",
    },
)
async def anim(shut):
    "Shut up"
    
    a = 1

    if a == 1 :
        fy = await edit_or_reply(shut,"Esh 😲...")
        time.sleep(3)
        fucki = await fy.edit(f"Esh 🤨...")
        time.sleep(9)
        await fucki.edit(f"Shut the fuck up 🤫")
    else:
      await edit_or_reply(f"Seems like something's wrong")
