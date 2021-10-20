# Ported from Ultroid Userbot by @kirito6969 for pepecat

import os

from PIL import Image

from . import catub, eod, eor

plugin_category = "tools"


@catub.cat_cmd(
    pattern="size$",
    command=("size", plugin_category),
    info={
        "header": "To Get size of it!",
        "description": "To Get size of it!",
        "usage": "{tr}size <reply to media>",
    },
)
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eod(e, "`Reply to image.`")
    k = await eor(e, "`Processing...`")
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    im = Image.open(img)
    x, y = im.size
    await k.edit(f"Dimension Of This Image Is\n`{x} x {y}`")
    os.remove(img)


@catub.cat_cmd(
    pattern="resize(?:\s|$)([\s\S]*)",
    command=("resize", plugin_category),
    info={
        "header": "Resize image on x, y axis",
        "usage": "{tr}resize <number> <number>\n{tr}resize 690 960",
    },
)
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eod(e, "`Reply to image.`")
    sz = e.pattern_match.group(1)
    if not sz:
        return await eod(f"Give Some Size To Resize, Like `{tr}resize 720 1080` ", 5)
    k = await eor(e, "`Processing...`")
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    sz = sz.split()
    if len(sz) != 2:
        return await eod(k, f"Give Some Size To Resize, Like `{tr}resize 720 1080` ", 5)
    x, y = int(sz[0]), int(sz[1])
    im = Image.open(img)
    ok = im.resize((x, y))
    ok.save(img, format="PNG", optimize=True)
    await e.reply(file=img)
    os.remove(img)
    await k.delete()
