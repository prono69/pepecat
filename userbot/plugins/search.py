# Made by @e3ris for Ultroid.
# Modified by @kirito6969 for pepecat

from . import catub, edit_delete, edit_or_reply

plugin_category = "tools"


@catub.cat_cmd(
    pattern="search( -r|) ?(.*)",
    command=("search", plugin_category),
    info={
        "header": "Search messages in chat.",
        "description": "You can search messages in any chat",
        "flags": {"-r": "To search messages in reverse order."},
        "usage": [
            "{tr}search <text>",
            "{tr}search -r <text> ; 5",
        ],
    },
)
async def searcher(e):
    eris = await edit_or_reply(e, "`Searching...`")
    if e.is_private:
        return await edit_delete(eris, "Try in some groups lol...")
    args = e.pattern_match.group(2)
    if not args or len(args) < 2:
        return await edit_delete(eris, "Invalid argument!, Try again")
    if ";" in args:
        args, limit = args.split(";", 1)
    try:
        limit = int(limit)
    except:
        limit = 5
    limit = min(limit, 99)
    text, c = "", 0
    async for msg in e.client.iter_messages(
        e.chat_id, search=args, limit=limit, reverse=bool(e.pattern_match.group(1))
    ):
        text += f" [»» {msg.id}](t.me/c/{e.chat.id}/{msg.id})\n"
        c += 1

    txt = (
        f"**Results for :**  `{args}` \n\n{text}"
        if c > 0
        else f"**No Results for :**  `{args}`"
    )
    await eris.edit(txt)
