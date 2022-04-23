# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "fun"

@catub.cat_cmd(
    pattern="superfban ?(.*)",
    command=("superfban",
    plugin_category),
      info={
        "header": "Super fbans the user ( fake )",
        "usage": "{tr}superfban <username/reply>",
    },
)
async def anim(superfban):
    "Super fbans the user"
    
    a = 1

    if a == 1 :
        msrprt = await edit_or_reply(superfban, "`Initiating super fban of the user...`")
        time.sleep(3)
        reporti = await sfb.edit(f"`Super fbanning the user...`")
        time.sleep(11)
        await superfbani.edit(f"Successfully super fbanned the user\n\nGet lost bloody fool")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
