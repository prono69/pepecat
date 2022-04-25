from telethon import functions

from userbot import catub

from ..Config import Config
from ..core import CMD_INFO, GRP_INFO, PLG_INFO
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

cmdprefix = Config.COMMAND_HAND_LER

plugin_category = "tools"

hemojis = {
    "admin": "👮🏻‍♀️",
    "bot": "💖",
    "fun": "🪄",
    "misc": "🔮",
    "tools": "🕸️",
    "utils": "🍻",
    "extra": "🕯️",
}


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


async def cmdinfo(input_str, event, plugin=False):
    if input_str[0] == cmdprefix:
        input_str = input_str[1:]
    try:
        about = CMD_INFO[input_str]
    except KeyError:
        if plugin:
            await edit_delete(
                event,
                f"There is no plugin or command as `{input_str}` in your bot",
            )
            return None
        await edit_delete(
            event, f"There is no command as `{input_str}` in your bot"
        )
        return None
    except Exception as e:
        await edit_delete(event, f"**Error :**\n`{e}`")
        return None
    outstr = f"Command : `{cmdprefix}{input_str}`\n"
    plugin = get_key(input_str)
    if plugin is not None:
        outstr += f"Plugin : `{plugin}`\n"
        category = getkey(plugin)
        if category is not None:
            outstr += f"Category : `{category}`\n\n"
    outstr += f"✘  Intro :\n{about[0]}"
    return outstr


async def plugininfo(input_str, event, flag):
    try:
        cmds = PLG_INFO[input_str]
    except KeyError:
        outstr = await cmdinfo(input_str, event, plugin=True)
        return outstr
    except Exception as e:
        await edit_delete(event, f"**Error :**\n`{e}`")
        return None
    if len(cmds) == 1 and (flag is None or (flag and flag != "-p")):
        outstr = await cmdinfo(cmds[0], event, plugin=False)
        return outstr
    outstr = f"Plugin : `{input_str}`\n"
    outstr += f"Commands available : `{len(cmds)}`\n"
    category = getkey(input_str)
    if category is not None:
        outstr += f"Category : `{category}`\n\n"
    for cmd in sorted(cmds):
        outstr += f"• Command : `{cmdprefix}{cmd}`\n"
        try:
            outstr += f"• Info : `{CMD_INFO[cmd][1]}`\n\n"
        except IndexError:
            outstr += "• Info : `None`\n\n"
    outstr += f"Usage : `{cmdprefix}help <command name>`\
        \nNote : If command name is same as plugin name then use this `{cmdprefix}help -c <command name>`"
    return outstr


async def grpinfo():
    outstr = "Plugins in catuserbot are :\n\n"
    outstr += f"Usage : `{cmdprefix}help <plugin name>`\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra"]
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"{hemojis[cat]} {cat.title()} ({len(plugins)})\n"
        for plugin in plugins:
            outstr += f"`{plugin}`  "
        outstr += "\n\n"
    return outstr


async def cmdlist():
    outstr = "Total list of commands in your catuserbot are :\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra", "useless"]
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"{hemojis[cat]} {cat.title()} - {len(plugins)}\n\n"
        for plugin in plugins:
            cmds = PLG_INFO[plugin]
            outstr += f"• {plugin.title()} has {len(cmds)} commands\n"
            for cmd in sorted(cmds):
                outstr += f"  - `{cmdprefix}{cmd}`\n"
            outstr += "\n"
    outstr += f"Usage : `{cmdprefix}help -c <command name>`"
    return outstr


@catub.cat_cmd(
    pattern="help ?(-c|-p|-t)? ?([\s\S]*)?",
    command=("help", plugin_category),
    info={
        "header": "To get guide for catuserbot",
        "description": "To get information or guide for the command or plugin",
        "note": "If command name and plugin name is same then you get guide for plugin so by using this flag you get command guide",
        "flags": {
            "c": "To get info of command",
            "p": "To get info of plugin",
            "t": "To get all plugins in text format",
        },
        "usage": [
            "{tr}help (plugin/command name)",
            "{tr}help -c (command name)",
        ],
        "examples": ["{tr}help help", "{tr}help -c help"],
    },
)
async def _(event):
    "To get guide for catuserbot"
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if flag and flag == "-c" and input_str:
        outstr = await cmdinfo(input_str, event)
        if outstr is None:
            return
    elif input_str:
        outstr = await plugininfo(input_str, event, flag)
        if outstr is None:
            return
    elif flag == "-t":
        outstr = await grpinfo()
    else:
        results = await event.client.inline_query(Config.TG_BOT_USERNAME, "help")
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
        return
    await edit_or_reply(event, outstr)


@catub.cat_cmd(
    pattern="cmds(?:\s|$)([\s\S]*)",
    command=("cmds", plugin_category),
    info={
        "header": "To show list of commands",
        "description": "If no input is given then will show list of all commands",
        "usage": [
            "{tr}cmds for all cmds",
            "{tr}cmds <plugin name> for paticular plugin",
        ],
    },
)
async def _(event):
    "To get list of commands"
    if input_str := event.pattern_match.group(1):
        try:
            cmds = PLG_INFO[input_str]
        except KeyError:
            return await edit_delete(event, "Invalid plugin name recheck it")
        except Exception as e:
            return await edit_delete(event, f"**Error :**\n`{e}`")
        outstr = f"• {input_str.title()} has {len(cmds)} commands\n"
        for cmd in cmds:
            outstr += f"  - `{cmdprefix}{cmd}`\n"
        outstr += f"Usage : `{cmdprefix}help -c <command name>`"
    else:
        outstr = await cmdlist()
    await edit_or_reply(
        event, outstr, aslink=True, linktext="Total commands of catuserbot are :"
    )


@catub.cat_cmd(
    pattern="s ([\s\S]*)",
    command=("s", plugin_category),
    info={
        "header": "To search commands",
        "examples": "{tr}s song",
    },
)
async def _(event):
    "To search commands"
    cmd = event.pattern_match.group(1)
    if found := [i for i in sorted(list(CMD_INFO)) if cmd in i]:
        out_str = "".join(f"`{i}`    " for i in found)
        out = f"I found {len(found)} command(s) for : `{cmd}`\n\n{out_str}"
        out += f"\n\nFor more info check {cmdprefix}help -c <command>"
    else:
        out = f"I can't find any such command `{cmd}` in catuserbot"
    await edit_or_reply(event, out)


@catub.cat_cmd(
    pattern="dc$",
    command=("dc", plugin_category),
    info={
        "header": "To show dc of your account",
        "description": "Dc of your account and list of dc's will be showed",
        "usage": "{tr}dc",
    },
)
async def _(event):
    "To get dc of your bot"
    result = await event.client(functions.help.GetNearestDcRequest())
    result = f"**Dc details of your account :**\
              \n**Country :** {result.country}\
              \n**Current dc :** {result.this_dc}\
              \n**Nearest dc :** {result.nearest_dc}\
              \n\n**List of telegram data centres :**\
              \n**Dc 1 : **Miami FL , USA\
              \n**Dc 2 :** Amsterdam , NL\
              \n**Dc 3 :** Miami FL , USA\
              \n**Dc 4 :** Amsterdam , NL\
              \n**Dc 5 : **Singapore , SG\
                "
    await edit_or_reply(event, result)
