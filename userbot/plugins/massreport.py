# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "fun"

@catub.cat_cmd(
    pattern="massreport ?(.*)",
    command=("massreport",
    plugin_category),
      info={
        "header": "Mass reports the user",
        "usage": "{tr}superfban <username/reply>",
    },
)
async def anim(superfban):
    "Mass reports the user"
    
    a = 1

    if a == 1 :
        msrt = await edit_or_reply(massreport, "`Initiating mass reporting of the user...`")
        time.sleep(3)
        reporti = await msrt.edit(f"`Mass reporting the user...`")
        time.sleep(11)
        await reporti.edit(f"Successfully mass reported the user\n\nYour account will be deleted soon\n\nReason : Toxic kids")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
