# From ultroid by @kirito6969

import asyncio
import os

import cv2
import requests

from ..core.managers import edit_delete, edit_or_reply
from . import catub

plugin_category = "extra"


@catub.cat_cmd(
    pattern="sketch$",
    command=("sketch", plugin_category),
    info={
        "header": "To draw its sketch.",
        "usage": ["{tr}sketch in reply to a photo"],
    },
)
async def sketch(e):
    "To draw its sketch."
    ureply = await e.get_reply_message()
    xx = await edit_or_reply(e, "`...`")
    if not (ureply and (ureply.media)):
        await edit_delete(event, "`Reply to any media`")
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
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(ultt)
        heh, lol = img.read()
        cv2.imwrite("ult.png", lol)
        file = "ult.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("ultroid.png", pencil_sketch_IMG)
    await e.client.send_file(e.chat_id, file="ultroid.png")
    await xx.delete()
    os.remove(file)
    os.remove("ultroid.png")


@catub.cat_cmd(
    pattern="toon$",
    command=("toon", plugin_category),
    info={
        "header": "To make it toon.",
        "usage": ["{tr}toon in reply to a photo"],
    },
)
async def ultd(event):
    "To make it toon."
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await edit_delete(event, "`Reply to any media`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith(".tgs"):
        await xx.edit("`OwO Animated sticker...👀`")
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
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(ultt)
        heh, lol = img.read()
        cv2.imwrite("ult.png", lol)
        file = "ult.png"
    ult = cv2.imread(file)
    height, width, channels = ult.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = ult[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    ish = centers[labels.flatten()]
    ultroid = ish.reshape(ult.shape)
    cv2.imwrite("ult.jpg", ultroid)
    await event.client.send_file(
        event.chat_id,
        "ult.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("ult.png")
    os.remove("ult.jpg")
    os.remove(ultt)


@catub.cat_cmd(
    pattern="danger$",
    command=("danger", plugin_category),
    info={
        "header": "To make it look Danger.",
        "usage": ["{tr}danger in reply to a photo"],
    },
)
async def ultd(event):
    "To make it look Danger."
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await edit_delete(event, "`Reply to any media`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith(".tgs"):
        await xx.edit("`OwO Animated sticker...👀`")
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
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(ultt)
        heh, lol = img.read()
        cv2.imwrite("ult.png", lol)
        file = "ult.png"
    ult = cv2.imread(file)
    dan = cv2.cvtColor(ult, cv2.COLOR_BGR2RGB)
    ultroid = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("ult.jpg", ultroid)
    await event.client.send_file(
        event.chat_id,
        "ult.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("ult.png")
    os.remove("ult.jpg")
    os.remove(ultt)


@catub.cat_cmd(
    pattern="quad$",
    command=("quad", plugin_category),
    info={
        "header": "Create a Vortex.",
        "usage": ["{tr}quad in reply to a photo"],
    },
)
async def ultd(event):
    "Create a Vortex."
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await edit_delete(event, "`Reply to any media`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith(".tgs"):
        await xx.edit("OwO Animated sticker...👀`")
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
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(ultt)
        heh, lol = img.read()
        cv2.imwrite("ult.png", lol)
        file = "ult.png"
    ult = cv2.imread(file)
    roid = cv2.flip(ult, 1)
    mici = cv2.hconcat([ult, roid])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    ultroid = cv2.vconcat([mici, trn])
    cv2.imwrite("ult.jpg", ultroid)
    await event.client.send_file(
        event.chat_id,
        "ult.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("ult.png")
    os.remove("ult.jpg")
    os.remove(ultt)


@catub.cat_cmd(
    pattern="icolor$",
    command=("icolor", plugin_category),
    info={
        "header": "To make it colorful.",
        "usage": ["{tr}icolor <reply to any Black nd White media>"],
    },
)
async def _(event):
    reply = await event.get_reply_message()
    if not reply.media:
        return await edit_delete(event, "`Reply To a Black nd White Image`")
    xx = await edit_or_reply(event, "`Coloring image 🎨🖌️...`")
    image = await reply.download_media()
    img = cv2.VideoCapture(image)
    ret, frame = img.read()
    cv2.imwrite("ult.jpg", frame)
    if Config.DEEP_AI is not None:
        key = Config.DEEP_AI
    else:
        key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={"image": open("ult.jpg", "rb")},
        headers={"api-key": key},
    )
    os.remove("ult.jpg")
    os.remove(image)
    if "status" in r.json():
        return await xx.edit(
            r.json()["status"] + "\nGet api nd set `{i}setvar DEEP_API key`"
        )
    r_json = r.json()["output_url"]
    await event.client.send_file(event.chat_id, r_json, reply_to=reply)
    await xx.delete()
