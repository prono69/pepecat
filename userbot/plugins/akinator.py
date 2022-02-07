# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# Original file can be found at https://github.com/TeamUltroid/Ultroid/blob/main/plugins/akinator.py
# Ported to cat userbot by t.me/realnub. If you remove these three lines then you are a pure 100% gay, real idiot and you will die in hell for sure.


import re

import akinator
from telethon import Button
from telethon.errors import BotMethodInvalidError
from telethon.events import CallbackQuery, InlineQuery

from userbot import catub

from ..core.decorators import check_owner

plugin_category = "fun"

games = {}
aki_photo = "https://telegra.ph/file/b0ff07069e8637783fdae.jpg"


@catub.cat_cmd(
    pattern="aki(?:\s|$)([\s\S]*)",
    command=("aki", plugin_category),
    info={
        "header": "Akinator game",
        "usage": "{tr}aki",
        "description": "Hmm, a game, try yourself!",
    },
)
async def doit(e):
    "Akinator game, try yourself."
    sta = akinator.Akinator()
    games.update({e.chat_id: {e.id: sta}})
    try:
        m = await e.client.inline_query(
            Config.TG_BOT_USERNAME, f"aki_{e.chat_id}_{e.id}"
        )
        await m[0].click(e.chat_id)
    except BotMethodInvalidError:
        return await e.send_file(
            e.chat_id, aki_photo, caption="**keep this and try again 😛**"
        )
    if e.out:
        await e.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"aki_?(.*)")))
@check_owner
async def doai(e):
    adt = e.pattern_match.group(1).decode("utf-8")
    dt = adt.split("_")
    ch = int(dt[0])
    mid = int(dt[1])
    await e.edit("`Processing...`")
    try:
        qu = games[ch][mid].start_game(child_mode=False)
        # child mode not should be promoted
    except KeyError:
        return await e.answer("`Game has been Terminated`", alert=True)
    bts = [Button.inline(o, f"aka_{adt}_{o}") for o in ["Yes", "No", "Idk"]]
    cts = [Button.inline(o, f"aka_{adt}_{o}") for o in ["Probably", "Probably Not"]]

    bts = [bts, cts]
    # ignored Back Button since it makes the Pagination looks Bad
    await e.edit(f"Q. {qu}", buttons=bts)


@catub.tgbot.on(CallbackQuery(data=re.compile(b"aka_?(.*)")))
@check_owner
async def okah(e):
    mk = e.pattern_match.group(1).decode("utf-8").split("_")
    ch = int(mk[0])
    mid = int(mk[1])
    ans = mk[2]
    try:
        gm = games[ch][mid]
    except KeyError:
        await e.answer("Timeout !")
        return
    text = gm.answer(ans)
    if gm.progression >= 80:
        gm.win()
        gs = gm.first_guess
        text = "It's " + gs["name"] + "\n " + gs["description"]
        return await e.edit(text, file=gs["absolute_picture_path"])
    bts = [Button.inline(o, f"aka_{ch}_{mid}_{o}") for o in ["Yes", "No", "Idk"]]
    cts = [
        Button.inline(o, f"aka_{ch}_{mid}_{o}") for o in ["Probably", "Probably Not"]
    ]

    bts = [bts, cts]
    await e.edit(text, buttons=bts)


@catub.tgbot.on(InlineQuery)
async def akigame(e):
    query_user_id = e.query.user_id
    query = e.text
    string = query.lower()
    if (
        query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS
    ) and string.startswith("aki"):
        ans = [
            await e.builder.photo(
                aki_photo,
                text=query,
                buttons=[Button.inline("Start Game", data=e.text)],
            )
        ]
        await e.answer(ans)
