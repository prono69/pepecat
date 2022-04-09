import asyncio
from collections import deque

from . import catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="think$",
    command=("think", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}think",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="lmao$",
    command=("lmao", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}lmao",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Lmao")
    deq = deque(list("🤣😝🤣😝🤣😝"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="nothappy$",
    command=("nothappy", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nothappy",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Nothappy")
    deq = deque(list("🥰😖🥰😖🥰😖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="clock$",
    command=("clock", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}clock",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="muah$",
    command=("muah", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}muah",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="heart$",
    command=("heart", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}heart",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="gym$",
    command=("gym", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gym",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="earth$",
    command=("earth", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}earth",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="moon$",
    command=("moon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}moon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "Moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@catub.cat_cmd(
    pattern="smoon$",
    command=("smoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}smoon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("Smoon...")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@catub.cat_cmd(
    pattern="tmoon$",
    command=("tmoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}tmoon",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("Tmoon...")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
