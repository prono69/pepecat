import re

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from . import AioHttp

plugin_category = "fun"

animal = r"([^.]*)$"
ok_exts = ["jpg", "jpeg", "png"]

animals_data = {
    "dog": {"url": "https://random.dog/woof.json", "key": "url"},
    "cat": {"url": "http://aws.random.cat/meow", "key": "file"},
    "panda": {"url": "https://some-random-api.ml/img/panda", "key": "link"},
    "redpanda": {"url": "https://some-random-api.ml/img/red_panda", "key": "link"},
    "bird": {"url": "https://some-random-api.ml/img/birb", "key": "link"},
    "fox": {"url": "https://some-random-api.ml/img/fox", "key": "link"},
    "koala": {"url": "https://some-random-api.ml/img/koala", "key": "link"},
}

animals = list(animals_data)


async def prep_animal_image(animal_data):
    ext = ""
    image = None
    while ext not in ok_exts:
        data = await AioHttp().get_json(animal_data["url"])
        image = data[animal_data["key"]]
        ext = re.search(animal, image).group(1).lower()
    return image


@catub.cat_cmd(
    pattern="animal ?(.*)",
    command=("animal", plugin_category),
    info={
        "header": "Sends you a beautiful animal picture ^_^",
        "usage": "{tr}animal [dog|cat|panda|redpanda|koala|bird|fox]",
        "examples": "{tr}animal cat",
    },
)
async def animal_image(message):
    lol = message.pattern_match.group(1)
    if not lol:
        await edit_delete(message, "`Are you really a Human ?`", 5)
        return
    animal_data = animals_data[lol]
    await message.client.send_file(
        message.chat_id,
        file=await prep_animal_image(animal_data),
        reply_to_id=message.reply_to_msg_id,
    )
    await message.delete()


@catub.cat_cmd(
    pattern="afact ?(.*)",
    command=("afact", plugin_category),
    info={
        "header": "Sends you an animal fact ^_^",
        "usage": "{tr}afact [dog|cat|panda|redpanda|koala|bird|fox]",
        "examples": "{tr}afact cat",
    },
)
async def fact(message):
    cmd = message.pattern_match.group(1)
    if not cmd:
        await edit_delete(message, "```Not enough params provided```", 5)
        return

    await edit_or_reply(message, f"```Getting {cmd} fact```")
    link = "https://some-random-api.ml/facts/{animal}"
    if cmd.lower() in animals:
        fact_link = link.format(animal=cmd.lower())
        try:
            data = await AioHttp().get_json(fact_link)
            fact_text = data["fact"]
        except Exception:
            await edit_delete(message, "```The fact API could not be reached```", 3)
        else:
            await edit_or_reply(message, f"__{cmd}__\n\n`{fact_text}`")
    else:
        await edit_delete(message, "`Unsupported animal...`", 3)
