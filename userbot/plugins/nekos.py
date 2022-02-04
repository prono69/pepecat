# #LazyAF_Geng
# By @kirito6969 for pepecat

"""NEKOS MODULE FOR PEPEBOT
\nPlugin Made by [NIKITA](https://t.me/kirito6969)
\n\n**DON'T EVEN TRY TO TO CHANGE CREDITS**'
"""

import os
import random

import nekos
import requests
from PIL import Image
from simplejson.errors import JSONDecodeError

from ..helpers.functions import age_verification
from . import (
    _catutils,
    catub,
    edit_delete,
    edit_or_reply,
    reply_id,
    useless,
    user_agent,
)

plugin_category = "fun"


SFW = [
    "awoo",
    "blush",
    "bully",
    "bite",
    "bonk",
    "cringe",
    "cry",
    "cuddle",
    "dance",
    "glomp",
    "handhold",
    "happy",
    "highfive",
    "hug",
    "kick",
    "kill",
    "kiss",
    "lick",
    "megumin",
    "neko",
    "nom",
    "pat",
    "poke",
    "shinobu",
    "slap",
    "smile",
    "smug",
    "waifu",
    "wave",
    "wink",
    "yeet",
]


NSFW = ["blowjob", "neko", "trap", "waifu"]

neko_help = "**🔞NSFW** :  "
for i in NSFW:
    neko_help += f"`{i.lower()}`   "
neko_help += "\n\n**😇SFW** :  "
for m in SFW:
    neko_help += f"`{m.lower()}`   "


@catub.cat_cmd(
    pattern="nn ?(.*)",
    command=("nn", plugin_category),
    info={
        "header": "Contains NSFW \nSearch images from nekos",
        "usage": "{tr}nn <argument from choice>",
        "examples": "{tr}nn neko",
        "options": useless.nsfw(useless.hemtai),
    },
)
async def _(event):
    "Search images from nekos"
    reply_to = await reply_id(event)
    choose = event.pattern_match.group(1)
    if choose not in useless.hemtai:
        return await edit_delete(
            event, "**Wrong Category!!**\nDo `.help -c nn` for Category list (*_*)`"
        )
    if await age_verification(event, reply_to):
        return
    catevent = await edit_or_reply(event, "`Processing Nekos...`")
    target = nekos.img(f"{choose}")
    nohorny = await event.client.send_file(
        event.chat_id, file=target, caption=f"**{choose}**", reply_to=reply_to
    )
    try:
        await _catutils.unsavegif(event, nohorny)
    except:
        pass
    await catevent.delete()


@catub.cat_cmd(
    pattern="dva$",
    command=("dva", plugin_category),
    info={
        "header": "Search dva images",
        "usage": "{tr}dva",
    },
)
async def dva(event):
    "Search dva images"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    try:
        nsfw = requests.get(
            "https://api.computerfreaker.cf/v1/dva",
            headers={"User-Agent": user_agent()},
        ).json()
        url = nsfw.get("url")
    except JSONDecodeError:
        return await edit_delete(
            event, "`uuuf.. seems like api down, try again later.`"
        )
    if not url:
        return await edit_delete(event, "`uuuf.. No URL found from the API`")
    await event.client.send_file(event.chat_id, file=url, reply_to=reply_to)
    await event.delete()


@catub.cat_cmd(
    pattern="nsfw$",
    command=("nsfw", plugin_category),
    info={
        "header": "NSFW \nSearch nsfw from nekos",
        "usage": "{tr}nsfw",
    },
)
async def avatarlewd(event):
    "NSFW. Search nsfw from nekos"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    with open("temp.png", "wb") as f:
        target = "nsfw_avatar"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()


@catub.cat_cmd(
    pattern="icat$",
    command=("icat", plugin_category),
    info={
        "header": "Search cute cats.",
        "usage": "{tr}icat",
    },
)
async def _(event):
    "Search cute cats."
    reply_to = await reply_id(event)
    target = nekos.cat()
    catevent = await edit_or_reply(event, "`Finding ur ket...`")
    await event.client.send_file(event.chat_id, file=target, reply_to=reply_to)
    await catevent.delete()


@catub.cat_cmd(
    pattern="lewdn$",
    command=("lewdn", plugin_category),
    info={
        "header": "NSFW \nSearch lewd nekos",
        "usage": "{tr}lewdn",
    },
)
async def lewdn(event):
    "NSFW.Search lewd nekos"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    nsfw = requests.get("https://nekos.life/api/lewd/neko").json()
    url = nsfw.get("neko")
    if not url:
        return await edit_delete(event, "`Uff.. No NEKO found from the API`")
    await event.client.send_file(event.chat_id, file=url, reply_to=reply_to)
    await event.delete()


@catub.cat_cmd(
    pattern="gasm$",
    command=("gasm", plugin_category),
    info={
        "header": "NSFW \nIt's gasm",
        "usage": "{tr}gasm",
    },
)
async def gasm(event):
    "NSFW. It's gasm"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    with open("temp.png", "wb") as f:
        target = "gasm"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()


@catub.cat_cmd(
    pattern="ifu$",
    command=("ifu", plugin_category),
    info={
        "header": "Search waifus from nekos",
        "usage": "{tr}ifu",
    },
)
async def waifu(event):
    "Search waifus from nekos"
    reply_to = await reply_id(event)
    with open("temp.png", "wb") as f:
        target = "waifu"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()


@catub.cat_cmd(
    pattern="ne ?(.*)",
    command=("ne", plugin_category),
    info={
        "header": "Contains NSFW \nSearch images from waifu.pics",
        "usage": "{tr}ne <argument from choice>",
        "examples": "{tr}ne cry",
        "options": neko_help,
    },
)
async def _(event):
    "Search images from waifu.pics"
    reply_to = await reply_id(event)
    choose = event.pattern_match.group(1)
    if choose == "":
        choose = random.choice(SFW)
    if choose in NSFW:
        type = "nsfw"
    else:
        type = "sfw"
    if choose not in neko_help:
        return await edit_delete(
            event, "**Wrong Category!!**\nDo `.help -c ne` for Category list (*_*)`"
        )
    if await age_verification(event, reply_to):
        return
    catevent = await edit_or_reply(event, "`Processing...`")
    resp = requests.get(f"https://api.waifu.pics/{type}/{choose}").json()
    target = resp.get("url")
    nohorny = await event.client.send_file(
        event.chat_id, file=target, caption=f"**{choose}**", reply_to=reply_to
    )
    try:
        await _catutils.unsavegif(event, nohorny)
    except:
        pass
    await catevent.delete()


ISFW = ["maid", "waifu"]

INSFW = [
    "ass",
    "ero",
    "hentai",
    "maid",
    "milf",
    "oppai",
    "oral",
    "paizuri",
    "selfies",
    "uniform",
    "ecchi",
]


waifu_help = "**🔞NSFW** :  "
for i in INSFW:
    waifu_help += f"`{i.lower()}`   "
waifu_help += "\n\n**😇SFW** :  "
for m in ISFW:
    waifu_help += f"`{m.lower()}`   "


@catub.cat_cmd(
    pattern="nm ?(.*)",
    command=("nm", plugin_category),
    info={
        "header": "Contains NSFW \nSearch images from waifu.im",
        "usage": "{tr}nm <argument from choice>",
        "examples": "{tr}nm waifu",
        "options": waifu_help,
    },
)
async def _(event):
    "Search images from waifu.im"
    reply_to = await reply_id(event)
    choose = event.pattern_match.group(1)
    if choose == "":
        choose = random.choice(ISFW)
    if choose in INSFW:
        type = "nsfw"
    else:
        type = "sfw"
    if choose not in waifu_help:
        return await edit_delete(
            event, "**Wrong Category!!**\nDo `.help -c nm` for Category list (*_*)`"
        )
    if await age_verification(event, reply_to):
        return
    catevent = await edit_or_reply(event, "`Processing...`")
    resp = requests.get(f"https://api.waifu.im/{type}/{choose}").json()
    target = resp["images"][0]["url"]
    nohorny = await event.client.send_file(
        event.chat_id, file=target, caption=f"**{choose}**", reply_to=reply_to
    )
    try:
        await _catutils.unsavegif(event, nohorny)
    except:
        pass
    await catevent.delete()
