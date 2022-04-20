from userbot import catub

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "Extra"


@catub.cat_cmd(
    pattern="upper(?: |$)([\s\S]*)",
    command=("upper", plugin_category),
    info={
        "header": "Text operation change to upper text",
        "usage": "{tr}upper <input text /reply to text>",
        "examples": "{tr}upper reply to valid text or give valid text as input",
    },
)
async def some(event):
    """Text format upper"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**Reply to valid text or give text as input ! You moron !**"
        )
    mystring = intxt.upper()
    await edit_or_reply(event, mystring)


@catub.cat_cmd(
    pattern="lower(?: |$)([\s\S]*)",
    command=("lower", plugin_category),
    info={
        "header": "Text operation change to lower text",
        "usage": "{tr}lower <input text /reply to text>",
        "examples": "{tr}lower reply to valid text or give valid text as input",
    },
)
async def good(event):
    """Text format lower"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**Reply to valid text or give text as input ! You moron !**"
        )
    mystring = intxt.lower()
    await edit_or_reply(event, mystring)


@catub.cat_cmd(
    pattern="title(?: |$)([\s\S]*)",
    command=("title", plugin_category),
    info={
        "header": "Text operation change to title text",
        "usage": "{tr}title<input text /reply to text>",
        "examples": "{tr}title Reply to valid text or give valid text as input",
    },
)
async def stuff(event):
    """Text format title"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**Reply to valid text or give text as input ! You moron !**"
        )
    mystring = intxt.title()
    await edit_or_reply(event, mystring)


@catub.cat_cmd(
    pattern="(|r)camel(?: |$)([\s\S]*)",
    command=("camel", plugin_category),
    info={
        "header": "Text operation change to camel text",
        "usage": [
            "{tr}camel <input text /reply to text>",
            "{tr}rcamel <input text /reply to text>",
        ],
        "examples": [
            "{tr}camel reply to valid text or give valid text as input",
            "{tr}rcamel reply to valid text or give valid text as input",
        ],
    },
)
async def here(event):
    """Text format camel"""
    cmd = event.pattern_match.group(1).lower()
    intxt = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**Reply to valid text or give text as input ! You moron !**"
        )
    if cmd == "r":
        bad = list(intxt.lower())[::2]
        cat = list(intxt.upper())[1::2]
    else:
        bad = list(intxt.upper())[::2]
        cat = list(intxt.lower())[1::2]
    mystring = "".join(f"{i}{j}" for i, j in zip(bad, cat))
    await edit_or_reply(event, mystring)
