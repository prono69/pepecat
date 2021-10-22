# Ported from Ultroid for pepecat by @kirito6969

import asyncio
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw

from . import catub, edit_delete, edit_or_reply

plugin_category = "extra"


@catub.cat_cmd(
    pattern="rund$",
    command=("rund", plugin_category),
    info={
        "header": "Make round stickers.",
        "usage": [
            "{tr}rund",
        ],
    },
)
async def ultdround(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`Processing...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", ultt, "ult.png"]
        file = "ult.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif ultt.endswith((".gif", ".mp4", ".mkv")):
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(ultt)
        heh, lol = img.read()
        cv2.imwrite("ult.png", lol)
        file = "ult.png"
    else:
        file = ultt
    img = Image.open(file).convert("RGB")
    npImage = np.array(img)
    h, w = img.size
    alpha = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    npAlpha = np.array(alpha)
    npImage = np.dstack((npImage, npAlpha))
    Image.fromarray(npImage).save("ult.webp")
    await event.client.send_file(
        event.chat_id,
        "ult.webp",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove(file)
    os.remove("ult.webp")


@catub.cat_cmd(
    pattern="tgs$",
    command=("tgs", plugin_category),
    info={
        "header": "Destory a sticker",
        "usage": "{tr}tgs <reply to a animated sticker>",
    },
)
async def tgscmd(message):
    """Tgs Killer"""
    reply = await message.get_reply_message()
    if not reply:
        await edit_delete(message, "`Reply to an animated sticker`", 3)
        return
    if not reply.file.name.endswith(".tgs"):
        await edit_delete(message, "`Reply to an animated sticker only.`", 3)
        return
    await reply.download_media("pepe.tgs")
    await edit_or_reply(message, "`Fixing this sticker...`")
    os.system("lottie_convert.py pepe.tgs json.json")
    json = open("json.json", "r")
    jsn = json.read()
    json.close()
    jsn = (
        jsn.replace("[100]", "[200]")
        .replace("[10]", "[40]")
        .replace("[-1]", "[-10]")
        .replace("[0]", "[15]")
        .replace("[1]", "[20]")
        .replace("[2]", "[17]")
        .replace("[3]", "[40]")
        .replace("[4]", "[37]")
        .replace("[5]", "[60]")
        .replace("[6]", "[70]")
        .replace("[7]", "[40]")
        .replace("[8]", "[37]")
        .replace("[9]", "[110]")
    )

    open("json.json", "w").write(jsn)
    os.system("lottie_convert.py json.json pepe.tgs")
    await message.reply(file="pepe.tgs")
    os.remove("json.json")
    os.remove("pepe.tgs")
    await message.delete()


@catub.cat_cmd(
    pattern="tiny$",
    command=("tiny", plugin_category),
    info={
        "header": "Make the replied sticker smol.",
        "usage": [
            "{tr}tiny <Reply to an animated sticker>",
        ],
    },
)
async def ultiny(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(event, "`Reply To Media`")
        return
    xx = await edit_or_reply(event, "`Processing...`")
    ik = await event.client.download_media(reply)
    im1 = Image.open("userbot/helpers/resources/ultroid_blank.png")
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
