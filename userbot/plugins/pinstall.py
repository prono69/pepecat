import os

import requests

from ..utils import load_module
from . import catub, edit_delete, edit_or_reply, reply_id

plugin_category = "tools"


@catub.cat_cmd(
    pattern="pinstall ([\s\S]*)",
    command=("pinstall", plugin_category),
    info={
        "header": "To install a plugin from master branch of your UPSTREAM_REPO , with just the name of plugin",
        "description": "Nice stuff",
        "usage": "{tr}pinstall <plugin name>",
    },
)
async def pure_brahness(event):
    "Directly install plugins from your repo with just the name"
    await reply_id(event)
    input_str = event.pattern_match.group(1)
    f"./userbot/plugins/{input_str}.py"
    repo_link = os.environ.get("UPSTREAM_REPO")
    if repo_link == "goodcat":
        repo_link = "https://github.com/sandy1709/catuserbot"
    if repo_link == "badcat":
        repo_link = "https://github.com/Jisan09/catuserbot"
    link = f"{repo_link}/raw/master/userbot/plugins/{input_str}.py"
    xx = await edit_or_reply(event, "`Processing...`")
    if link is None:
        return await edit_delete(xx, "`Give raw link or die !")
    split_link = link.split("/")
    if "raw" not in link:
        return await edit_delete(xx, "`Give raw link or die !")
    name = split_link[(len(split_link) - 1)]
    plug = requests.get(link).text
    fil = f"userbot/plugins/{name}"
    with open(fil, "w", encoding="utf-8") as pepe:
        pepe.write(plug)
    shortname = name.split(".")[0]
    try:
        load_module(shortname)
        await edit_delete(xx, "**Sᴜᴄᴄᴇssғᴜʟʟʏ Lᴏᴀᴅᴇᴅ** `{}`".format(shortname), 15)
    except Exception as e:
        await edit_delete(xx, f"Error with {shortname}\n`{e}`")
