# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the General Public License, Version 3.0;
# you may not use this file except in compliance with the License.
#
# Kamged from Nitesh Raj

import os

import numpy as np
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
from telethon.tl.types import DocumentAttributeFilename
from wordcloud import ImageColorGenerator, WordCloud

from ..core.managers import edit_delete, edit_or_reply
from . import catub

plugin_category = "extra"


@catub.cat_cmd(
    pattern="wwc",
    command=("wwc", plugin_category),
    info={
        "header": "It's Mejik",
        "description": "Huehue! Try yourself! 🌚",
        "usage": "{tr}wwc <reply to a image/sticker/video>",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await edit_delete(event, "`Are you mad Bish! Reply to Any media..`", 3)
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_delete(event, "`Reply to a image/sticker/video`", 3)
        return
    await edit_or_reply(event, "`Downloading Media..`")
    if reply_message.photo:
        await bot.download_media(
            reply_message,
            "wc.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "wc.tgs",
        )
        os.system("lottie_convert.py wc.tgs wc.png")
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "wc.mp4",
        )
        extractMetadata(createParser(video))
        os.system("ffmpeg -i wc.mp4 -vframes 1 -an -s 480x360 -ss 1 wc.png")
    else:
        await bot.download_media(
            reply_message,
            "wc.png",
        )
    try:
        await edit_or_reply(event, "`Processing...`")
        text = open("userbot/helpers/resources/alice.txt", encoding="utf-8").read()
        image_color = np.array(Image.open("wc.png"))
        image_color = image_color[::1, ::1]
        image_mask = image_color.copy()
        image_mask[image_mask.sum(axis=2) == 0] = 255
        edges = np.mean(
            [
                gaussian_gradient_magnitude(image_color[:, :, i] / 255.0, 2)
                for i in range(3)
            ],
            axis=0,
        )
        image_mask[edges > 0.08] = 255
        wc = WordCloud(
            max_words=2000,
            mask=image_mask,
            max_font_size=40,
            random_state=42,
            relative_scaling=0,
        )
        wc.generate(text)
        image_colors = ImageColorGenerator(image_color)
        wc.recolor(color_func=image_colors)
        wc.to_file("wc.png")
        await event.client.send_file(
            event.chat_id,
            "wc.png",
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        os.system("rm *.png *.mp4 *.tgs *.webp")
    except BaseException as e:
        os.system("rm *.png *.mp4 *.tgs *.webp")
        return await event.edit(str(e))
