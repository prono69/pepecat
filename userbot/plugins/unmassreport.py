# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "admin"

@catub.cat_cmd(
    pattern="unmassreport ?(.*)",
    command=("unmassreport",
    plugin_category),
      info={
        "header": "Unmass reports the user",
        "usage": "{tr}unmassreport <username/reply>",
    },
)
async def anim(report):
    "Unmass reports the user"
    
    a = 1

    if a == 1 :
        unmsrprt = await edit_or_reply(unreport, "`Initiating unmass report of the `[user](tg://user?id={user.id}) `in {len(san)} groups`")
        time.sleep(3)
        unreporti = await unmsrprt.edit(f"[{user.first_name}](tg://user?id={user.id}) `was unmass reported in {count} groups in {cattaken} seconds`\n\n**Reason :** `{reason}`")
        time.sleep(11)
        await unreporti.edit(f"[{user.first_name}](tg://user?id={user.id}) `was unmass reported in {count} groups in {cattaken} seconds`")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
