#By @yuki
import os
from PIL import Image, ImageEnhance
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@catub.cat_cmd(
    pattern="shade ?(.*)",
    command=("shade", plugin_category),
    info={
        "header": "Shades or darken photos",
        "description": "Reply to an image to dark it",
         "flags": {
            "d": "Dead mode",
        },
        "usage": [
            "{tr}shade <reply a pic>",
            "{tr}shade d <reply a pic>",
        ],
    },
)
async def shade(deep):
    "Darkener"
    if deep.fwd_from:
        return
    await deep.edit("`Processing...`")
    mode = deep.pattern_match.group(1)
    if mode == "d": factor = 0.1
    else: factor = 0.5
    reply_to_id = await reply_id(deep)
    get = await deep.get_reply_message()
    if not get:
    	return await edit_delete(deep, "`Please reply a photo`", 5)
    if not get.photo:
    	return await edit_delete(deep, "`Please reply a photo`", 5)
    else:
    	dl = await deep.client.download_media(get)
    	img = Image.open(dl)
    	bw = img.convert('L')
    	enhancer = ImageEnhance.Brightness(bw)
    	output = enhancer.enhance(factor)
    	end = output.save("Shade.png")
    	await deep.client.send_file(deep.chat_id, file="Shade.png", reply_to=reply_to_id)
    	await deep.delete()
    	os.remove(dl)
    	os.remove("Shade.png")
