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
        "usage": "{tr}massreport <username/reply>",
    },
)
async def anim(report):
    "Mass report user"
    
    a = 1

    if a == 1 :
        msrprt = await edit_or_reply(report, "`Initiating mass report of the `[user](tg://user?id={user.id}) `in {len(san)} groups`")
        time.sleep(3)
        reporti = await msrprt.edit(f"[{user.first_name}](tg://user?id={user.id}) `was mass reported in {count} groups in {cattaken} seconds`\n\n**Reason :** `{reason}`")
        time.sleep(11)
        await reporti.edit(f"[{user.first_name}](tg://user?id={user.id}) `was mass reported in {count} groups in {cattaken} seconds`")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
