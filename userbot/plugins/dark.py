# By @FeelDeD
import os

from PIL import Image, ImageEnhance

from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="dark ?(.*)",
    command=("dark", plugin_category),
    info={
        "header": "Photo/Sticker darkener",
        "description": "Reply to Photo/Sticker to dark it",
        "flags": {
            "d": "Dead mode",
        },
        "usage": [
            "{tr}dark <reply a pic/sticker>",
            "{tr}dark d <reply a pic/sticker>",
        ],
    },
)
async def dark(odi):
    "Darkener"
    if odi.fwd_from:
        return
    await odi.edit("`Processing ...`")
    mode = odi.pattern_match.group(1)
    factor = 0.1 if mode == "d" else 0.5
    reply_to_id = await reply_id(odi)
    get = await odi.get_reply_message()
    if not get:
        return await edit_delete(odi, "`Please reply a photo/sticker`", 5)
    if get.photo:
        name = "Dark.png"
    elif "tgsticker" in get.media.document.mime_type:
        return await edit_delete(odi, "`Please reply a photo/sticker`", 5)
    else:
        name = "Dark.webp"
    if get.photo or get.sticker:
        dl = await odi.client.download_media(get)
        img = Image.open(dl)
        bw = img.convert("L")
        enhancer = ImageEnhance.Brightness(bw)
        output = enhancer.enhance(factor)
        output.save(name)
        await odi.client.send_file(odi.chat_id, file=name, reply_to=reply_to_id)
        await odi.delete()
        os.remove(dl)
        os.remove(name)
    else:
        return await edit_delete(odi, "`Please reply a photo/sticker`", 5)
