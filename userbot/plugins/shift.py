# By @sakku
from .. import catub
from ..core.managers import edit_or_reply

plugin_category = "tools"


@catub.cat_cmd(
    pattern="shift (.*)",
    command=("shift", plugin_category),
    info={
        "header": "Beware danger ahead",
        "description": "To copy all messages or files from a channel or group to your channel or group",
        "usage": "{tr}shift <id of source group/channel> | <id of destination group/channel>",
        "examples": "{tr}shift -100|-100",
    },
)
async def _(e):
    x = e.pattern_match.group(1)
    z = await edit_or_reply(e, "Processing...")
    a, b = x.split("|")
    try:
        c = int(a)
    except Exception:
        try:
            c = (await bot.get_entity(a)).id
        except Exception:
            await z.edit("Invalid channel given")
            return
    try:
        d = int(b)
    except Exception:
        try:
            d = (await bot.get_entity(b)).id
        except Exception:
            await z.edit("Invalid channel given")
            return
    async for msg in bot.iter_messages(int(c), reverse=True):
        try:
            await asyncio.sleep(1.5)
            await bot.send_message(int(d), msg)
        except BaseException:
            pass
    await z.edit("Done")
