# Urban Dictionary for catuserbot by @mrconfused
from PyDictionary import PyDictionary

from userbot import catub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import AioHttp
from ..helpers.utils import _format

LOGS = logging.getLogger(__name__)
plugin_category = "utils"
dictionary = PyDictionary()


@catub.cat_cmd(
    pattern="ud ([\s\S]*)",
    command=("ud", plugin_category),
    info={
        "header": "To fetch meaning of the given word from urban dictionary.",
        "usage": "{tr}ud <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from urban dictionary."
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n`{}`\n\n**Example:**\n`{}`".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await edit_or_reply(event, result)
    except Exception as e:
        await edit_delete(
            event,
            text="`The Urban Dictionary API could not be reached`",
        )
        LOGS.info(e)


@catub.cat_cmd(
    pattern="meaning ([\s\S]*)",
    command=("meaning", plugin_category),
    info={
        "header": "To fetch meaning of the given word from dictionary.",
        "usage": "{tr}meaning <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from dictionary."
    word = event.pattern_match.group(1)
    cat = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in cat.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Couldn't fetch meaning of {word}")


@catub.cat_cmd(
    pattern="synonym ([\s\S]*)",
    command=("synonym", plugin_category),
    info={
        "header": "Get all synonyms of a word.",
        "usage": "{tr}synonym <word>",
    },
)
async def mean(event):
    evid = event.message.id
    xx = await edit_or_reply(event, "`Processing...`")
    wrd = event.pattern_match.group(1)
    ok = dictionary.synonym(wrd)
    x = f"**Word** - `{wrd}`\n\n**Synonyms** - \n"
    c = 1
    try:
        for i in ok:
            x += f"**{c}.** `{i}`\n"
            c += 1
        if len(x) > 4096:
            with io.BytesIO(str.encode(x)) as fle:
                fle.name = f"{wrd}-synonyms.txt"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption=f"Synonyms of {wrd}",
                    reply_to=evid,
                )
                await xx.delete()
        else:
            await xx.edit(x)
    except Exception as e:
        await xx.edit(f"No synonym found!!\n{str(e)}")


@catub.cat_cmd(
    pattern="antonym ([\s\S]*)",
    command=("antonym", plugin_category),
    info={
        "header": "Get all antonyms of a word.",
        "usage": "{tr}antonym <word>",
    },
)
async def mean(event):
    evid = event.message.id
    xx = await edit_or_reply(event, "`Processing...`")
    wrd = event.pattern_match.group(1)
    ok = dictionary.antonym(wrd)
    x = f"**Word** - `{wrd}`\n\n**Antonyms** - \n"
    c = 1
    try:
        for i in ok:
            x += f"**{c}.** `{i}`\n"
            c += 1
        if len(x) > 4096:
            with io.BytesIO(str.encode(x)) as fle:
                fle.name = f"{wrd}-antonyms.txt"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption=f"Antonyms of {wrd}",
                    reply_to=evid,
                )
                await xx.delete()
        else:
            await xx.edit(x)
    except Exception as e:
        await xx.edit(f"No antonym found!!\n{str(e)}")
