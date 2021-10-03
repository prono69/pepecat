# By @kirito6969
import re
from . import AioHttp, catub, eor, eod

plugin_category = "fun"

animal = r"([^.]*)$"
ok_exts = ["jpg", "jpeg", "png"]

animals_data = {
    "dog": {"url": "https://some-random-api.ml/animal/dog", "key": "image"},
    "cat": {"url": "http://aws.random.cat/meow", "key": "file"},
    "panda": {"url": "https://some-random-api.ml/img/panda", "key": "link"},
    "redpanda": {"url": "https://some-random-api.ml/img/red_panda", "key": "link"},
    "bird": {"url": "https://some-random-api.ml/img/birb", "key": "link"},
    "fox": {"url": "https://some-random-api.ml/img/fox", "key": "link"},
    "koala": {"url": "https://some-random-api.ml/img/koala", "key": "link"},
    "kangaroo": {"url": "https://some-random-api.ml/animal/kangaroo", "key": "image"},
    "racoon": {"url": "https://some-random-api.ml/animal/racoon", "key": "image"},
    
}

animals_with_facts = ['dog', 'cat', 'panda', 'fox', 'bird', 'koala', 'kangaroo', 'racoon', 'elephant', 'giraffe',
                      'whale']

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
    await eor(message, f"`Finding a cute {lol}...`")
    if not lol:
        await eod(message, "`Are you really a Human ?`", 5)
        return
    animal_data = animals_data[lol]
    if lol.lower() in animal_data:
      await message.client.send_file(message.chat_id, file=await prep_animal_image(animal_data), reply_to_id=message.reply_to_msg_id,)
      await message.delete()
    else:
      await eod(message, "`Unsupported Animal`", 3)


@catub.cat_cmd(
    pattern="afact ?(.*)",
    command=("afact", plugin_category),
    info={
        "header": "Sends you an animal fact ^_^",
        "usage": "{tr}afact [dog|cat|panda|redpanda|koala|bird|fox|kangaroo|racoon|elephant|giraffe|whale]",
        "examples": "{tr}afact cat",
    },
)
async def fact(message):
    cmd = message.pattern_match.group(1)
    if not cmd:
        await eod(message, "```Not enough params provided```", 5)
        return

    await eor(message, f"```Getting {cmd} fact```")
    link = "https://some-random-api.ml/facts/{animal}"
    if cmd.lower() in animals_with_facts:
        fact_link = link.format(animal=cmd.lower())
        try:
            data = await AioHttp().get_json(fact_link)
            fact_text = data["fact"]
        except Exception:
            await eod(message, "```The fact API could not be reached```", 3)
        else:
            await eod(message, f"**{cmd}**\n\n`{fact_text}`")
    else:
        await eod(message, "`Unsupported animal...`", 3)
