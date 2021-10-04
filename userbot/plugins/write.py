import os

from PIL import Image, ImageDraw, ImageFont

from userbot import catub

from ..helpers.utils import edit_delete

plugin_category = "extra"


@catub.cat_cmd(
    pattern="write(?:\s|$)([\s\S]*)",
    command=("write", plugin_category),
    info={
        "header": "To write given text or replied message on paper.",
        "usage": "{tr}write <message/reply>",
        "examples": "{tr}write Hello World",
    },
)
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(e, "`Give Some Text`")
    await edit_delete(e, "`Writing wait....`")
    img = Image.open("userbot/helpers/resources/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("userbot/helpers/styles/assfont.ttf", 30)
    x, y = 150, 140
    line_height = font.getsize("hg")[1]
    draw.text((x, y), text, fill=(1, 22, 55), font=font)
    y = y + line_height - 5
    file = "pic.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
