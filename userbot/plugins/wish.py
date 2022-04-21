# Made by @yuki

import random

from ..core.managers import edit_or_reply
from . import catub

plugin_category = "extra"


@catub.cat_cmd(
    pattern="wish ?(.*)",
    command=("wish", plugin_category),
    info={
        "header": "Wish someone",
        "usage": "{tr}wish <your wish>",
    },
)
async def LEGENDBOT(event):
    LEGENDX = event.pattern_match.group(1)
    PROBOY = random.randint(0, 100)
    if LEGENDX:
        reslt = f"""🦋 ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱ ʙᴇᴇɴ ᴄᴀꜱᴛᴇᴅ 🦋\n\n\n 𝕐𝕠𝕦𝕣 𝕨𝕚𝕤𝕙 ➪ **`{LEGENDX}`** 
              \n\n𝐂𝐇𝐀𝐍𝐂𝐄 𝐎𝐅 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 : **{PROBOY}%**"""
    else:
        if event.is_reply:
            reslt = f"🦋 ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱ ʙᴇᴇɴ ᴄᴀꜱᴛᴇᴅ 🦋\
                 \n\n𝐂𝐇𝐀𝐍𝐂𝐄 𝐎𝐅 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 : {PROBOY}%"
        else:
            reslt = f"🦋 ʏᴏᴜʀ ᴡɪꜱʜ ʜᴀꜱ ʙᴇᴇɴ ᴄᴀꜱᴛᴇᴅ 🦋\
                  \n\n𝐂𝐇𝐀𝐍𝐂𝐄 𝐎𝐅 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 : {PROBOY}%"
    await edit_or_reply(event, reslt)
