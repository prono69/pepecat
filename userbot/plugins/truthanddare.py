# By @yuki

import requests as r
from bs4 import BeautifulSoup as bs

from ..core.managers import edit_or_reply
from . import catub

plugin_category = "extra"

link = "https://fungenerators.com/random/truth-or-dare?option="


@catub.cat_cmd(
    pattern="truth",
    command=("truth", plugin_category),
    info={
        "header": "Get random truth task",
        "usage": "{tr}truth",
    },
)
async def gtruth(deep):
    m = await edit_or_reply(deep, "Generating a truth statement.. ")
    nl = link + "truth"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"#TruthTask\n\n{cm}")


@catub.cat_cmd(
    pattern="dare",
    command=("dare", plugin_category),
    info={
        "header": "Get random dare task",
        "usage": "{tr}dare",
    },
)
async def gtruth(deep):
    m = await edit_or_reply(deep, "Generating a dare task.. ")
    nl = link + "dare"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"#DareTask\n\n{cm}")
