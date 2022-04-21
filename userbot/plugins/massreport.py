# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "fun"

@catub.cat_cmd(
    pattern="massreport ?(.*)",
    command=("mreport",
    plugin_category),
      info={
        "header": "Mass reports user ( fake )",
        "usage": "{tr}massreport <username/reply>",
    },
)
async def anim(report):
    "Mass report user"
    
    a = 1

    if a == 1 :
        msrprt = await edit_or_reply(report, "`Initiating mass report of user...`")
        time.sleep(3)
        reporti = await msrprt.edit(f"`Mass reporting user...`")
        time.sleep(11)
        await reporti.edit(f"Mass reported user")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
