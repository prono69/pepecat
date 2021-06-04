# made by @Alain_Champion and TEAMLEGEND
# Credites :- @LEGENDX22 , @PROBOYX
# if you kang this please keep credits

import random

from ..core.managers import edit_or_reply
from . import catub


@catub.cat_cmd(
    pattern="wish ?(.*)",
    command=("wish", plugin_category),
    info={
        "header": "Wish someone LOL",
        "usage": "{tr}wish <your wish>",
    },
)
async def LEGENDBOT(event):
    LEGENDX = event.pattern_match.group(1)
    PROBOY = random.randint(0, 100)
    if LEGENDX:
        reslt = f"""🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\n\n\n☘️ 𝐘𝐨𝐮𝐫 𝐖𝐢𝐬𝐡 ➪ **`{LEGENDX}`** ✨
              \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : **{PROBOY}%**"""
    else:
        if event.is_reply:
            reslt = f"🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\
                 \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : {PROBOY}%"
        else:
            reslt = f"🦋 Yᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛᴇᴅ 🦋\
                  \n\n🔥𝙲𝙷𝙰𝙽𝙲𝙴 𝙾𝙵 𝚂𝚄𝙲𝙲𝙴𝚂𝚂 : {PROBOY}%"
    await edit_or_reply(event, reslt)
