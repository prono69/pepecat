# Made by @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "admin"

@catub.cat_cmd(
    pattern="superfban ?(.*)",
    command=("superfban",
    plugin_category),
      info={
        "header": "Super fbans the user",
        "usage": "{tr}superfban <username/reply>",
    },
)
async def anim(fban):
    "Super fbans the user"
    
    a = 1

    if a == 1 :
        superfban = await edit_or_reply(fban, "`Initiating super fban of the `[user](tg://user?id={user.id}) `in {len(san)} groups`")
        time.sleep(3)
        fbani = await superfban.edit(f"`[{user.first_name}](tg://user?id={user.id}) `was super fbanned in {count} groups in {cattaken} seconds`\n\n**Reason :** `{reason}`")
        time.sleep(11)
        await fbani.edit(f"[{user.first_name}](tg://user?id={user.id}) `was super fbanned in {count} groups in {cattaken} seconds`")
    else:
    	await edit_or_reply(f"Seems like something's wrong")
