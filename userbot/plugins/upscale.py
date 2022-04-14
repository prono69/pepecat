import os

import requests

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from . import reply_id

plugin_category = "extra"


def upPic(img):
    r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        files={
            "image": open(img, "rb"),
        },
        headers={"api-key": "39678a25-4960-41ea-9bd7-4c8bbc4740eb"},
    )
    waifu_ed = r.json()["output_url"]
    os.system(f"rm {img}")
    return waifu_ed


def upLink(img):
    link = upPic(img)
    r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        data={
            "image": link,
        },
        headers={"api-key": "39678a25-4960-41ea-9bd7-4c8bbc4740eb"},
    )
    waifu_ed = r.json()["output_url"]
    return waifu_ed


@catub.cat_cmd(
    pattern="up$",
    command=("up", plugin_category),
    info={
        "header": "Upscale images",
        "usage": "{tr}up <reply to image>",
        "note": "Works better on anime pics",
    },
)
async def waifuu(event):
    "Upscale images"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        await edit_delete(event, "Reply to pic brah.")
        return
    try:
        name = reply.file.mime_type
    except:
        name = None
    if "image" in name:
        if "webp" in name:
            await edit_or_reply(event, "`Don't support sticker currently.`")
        await edit_or_reply(event, "`Upscaling...`")
        if ("jpeg" or "jpg") in name:
            img = await reply.download_media("waifu.jpg")
        elif "png" in name:
            img = await reply.download_media("waifu.png")
        waifu_ed = upPic(img)
        await edit_or_reply(event, "`Uploading...`")
        await event.client.send_file(
            event.chat.id, file=waifu_ed, force_document=True, reply_to=reply_to_id
        )
        await event.delete()

    else:
        await edit_delete(event, "BRAh.")


@catub.cat_cmd(
    pattern="upx$",
    command=("upx", plugin_category),
    info={
        "header": "Upscale images 2 times",
        "usage": "{tr}upx <reply to image>",
        "note": "Works better on anime pics",
    },
)
async def waifuu(event):
    "Upscale images 2 times"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        await edit_delete(event, "Reply to pic brah.")
        return
    try:
        name = reply.file.mime_type
    except:
        name = None
    if "image" in name:
        await edit_or_reply(event, "`Upscaling 2x...`")
        if ("jpeg" or "jpg") in name:
            img = await reply.download_media("waifu.jpg")
        elif "png" in name:
            img = await reply.download_media("waifu.png")
        waifu_ed = upLink(img)
        await edit_or_reply(event, "`Uploading...`")
        await event.client.send_file(
            event.chat.id, file=waifu_ed, force_document=True, reply_to=reply_to_id
        )
        await event.delete()

    else:
        await edit_delete(event, "BRAh.")
