# By @yuki

import asyncio
import os
import urllib
import requests
from PIL import Image, ImageDraw
from . import *
import os
try:
    import cv2
except ModuleNotFoundError:
    os.system("pip3 install opencv-python")
    import cv2
plugin_category = "extra"

@catub.cat_cmd(
    pattern="tiny$",
    command=("tiny", plugin_category),
    info={
        "header": "Make the replied sticker small",
        "usage": [
            "{tr}tiny <Reply to a sticker>",
        ],
    },
)
async def ultiny(event):
    "Tiny sticker gen"
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(event, "Reply to media")
        return
    xx = await edit_or_reply(event, "Processing...")
    ik = await event.client.download_media(reply)
    blank = "downloads/ultroid_blank.png"
    if os.path.exists("downloads/ultroid_blank.png"):
        os.remove(blank)
    urllib.request.urlretrieve("https://github.com/prono69/pepecat/raw/master/userbot/helpers/resources/ultroid_blank.png",blank)
    im1 =  Image.open(blank)
    if ik.endswith(".tgs"):
        await event.client.download_media(reply, "ult.tgs")
        os.system("lottie_convert.py ult.tgs json.json")
        with open("json.json") as json:
            jsn = json.read()
        jsn = jsn.replace("512", "1000")
        open("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(ik)
