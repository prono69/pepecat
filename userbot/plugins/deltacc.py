# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "extra"

@catub.cat_cmd(
    pattern="deltacc ?(.*)",
    command=("deltacc",
    plugin_category),
      info={
        "header": "Deletes the telegram account of the user",
        "usage": "{tr}deltacc <username/reply>",
    },
)
async def anim(delete):
    "Deletes the telegram account of the user"
    
    a = 1

    if a == 1 :
        accdlt = await edit_or_reply(delete, "Initiating deletion of telegram account of the user...")
        time.sleep(2)
        deletei = await accdlt.edit(f"Deleting telegram account of the user in few seconds...")
        time.sleep(4)
        await deletei.edit(f"Congratulations your telegram account has been deleted\n\nReason : Toxic , pm spammer , scammer , adding spambots , illegal , crimes against girls , blackmailer , ban evasion , raid participant etc\n\nRest in peace kid 😤")
    else:
      await edit_or_reply(f"Seems like something's wrong")
