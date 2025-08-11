"""Tools for lazy devs"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import asyncio
import importlib
import inspect
import io
import os
import sys
import traceback

from ..helpers.utils import _format, json_parser
from . import *

plugin_category = "tools"
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@catub.cat_cmd(
    pattern="bash(?:\s|$)([\s\S]*)",
    command=("bash", plugin_category),
    info={
        "header": "To Execute terminal commands in a subprocess.",
        "usage": "{tr}bash <command>",
        "examples": "{tr}bash cat stringsetup.py",
    },
)
async def _(event):
    "To Execute terminal commands in a subprocess."
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await edit_delete(event, "`What should i execute?..`")
    catevent = await edit_or_reply(event, "`Executing.....`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    catuser = await event.client.get_me()
    curruser = catuser.username or "catuserbot"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"**{curruser}:~#** \n`{cmd}`\n\n**• OUTPUT:**\n`{result}`"
    else:
        cresult = f"```{curruser}:~$``` ```{cmd}```\n```{result}```"
    await edit_or_reply(
        catevent,
        text=cresult,
        aslink=True,
        linktext=f"**•  Exec : **\n`{cmd}` \n\n**•  Result : **\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"**Terminal command executed successfully:**\n\n```{cmd}```"
        )


@catub.cat_cmd(
    pattern="eval(?:\s|$)([\s\S]*)",
    command=("eval", plugin_category),
    info={
        "header": "To Execute python script/statements in a subprocess.",
        "usage": "{tr}eval <command>",
        "examples": "{tr}eval print('catuserbot')",
    },
)
async def _(event):
    "To Execute python script/statements in a subprocess."
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return await edit_delete(event, "`What should i run ?..`")
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    catevent = await edit_or_reply(event, "`Running ...`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = await reply_id(event)
    try:
        value = await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = exc or stderr or stdout or _parse_eval(value) or "Success"
    final_output = (
        f"__►__ **Eval : **\n`{cmd}` \n\n__►__ **Result : **\n`{evaluation}` \n"
    )
    if len(final_output) > 4096:
        neko = final_output.replace("`", "").replace("**", "").replace("__", "")
        with io.BytesIO(str.encode(neko)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb=thumb_image_path,
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
        return await catevent.delete()
    await edit_or_reply(event, final_output)

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"**Eval command executed successfully:**\n\n```{cmd}```"
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    r = reply
    exec(
        (
            "async def __aexec(message, event , reply, r, client, p, chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, r, message.client, p, message.chat_id
    )


def _parse_eval(value):
    if value is None:
        return
    if hasattr(value, "stringify"):
        try:
            return value.stringify()
        except TypeError:
            pass
    elif isinstance(value, dict):
        try:
            return json_parser(value, indent=4)
        except BaseException:
            pass
    # is to_dict is also Good option to format?
    return str(value)


@catub.cat_cmd(
    pattern="inspect ([\s\S]*)",
    command=("inspect", plugin_category),
    info={
        "header": "To search any function/plugin/class",
        "description": "Searches the function/plugin/class and send in text file.",
        "usage": [
            "{tr}inspect <module>",
            "{tr}inspect <function>",
            "{tr}inspect <module> <function>",
        ],
        "examples": [
            "{tr}inspect userbot.plugins.alive",
            "{tr}inspect edit_or_reply",
            "{tr}inspect bs4 BeautifulSoup",
        ],
    },
)
async def search_func(event):
    "To inspect source"
    query = event.pattern_match.group(1)
    if not query:
        return await edit_delete(event, "`Give me source.....`")
    catevent = await edit_or_reply(event, "`Processing.....`")
    try:
        source = eval(query)
        filename = f"{query}.txt"
    except (NameError, SyntaxError):
        module_name, *function = query.split()
        function = function[0] if function else None
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            return await edit_delete(
                catevent,
                f"**Error:**  no module or function found by the name: {module_name}",
            )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if function:
            attributes = dir(module)
            if function not in attributes:
                for _, obj in inspect.getmembers(module, inspect.isclass):
                    attributes = dir(obj)
                    if function in attributes:
                        source = getattr(obj, function)
                        break
                else:
                    return await edit_delete(
                        catevent,
                        f"**Error:**  function: {function} not found in module: {module_name}",
                    )
            else:
                source = getattr(module, function)
            filename = f"{function}.txt"
        else:
            filename = module_name.split(".")[-1] + ".txt"
            source = module

    filepath = inspect.getfile(source)
    caption = f"**Source:**  `{filepath}`"
    text = inspect.getsource(source)
    if len(text) > 4096:
        with open(filename, "w") as f:
            f.write(text)
            await catub.send_file(
                event.chat_id,
                filename,
                caption=caption,
                allow_cache=False,
                reply_to=event.message.reply_to_msg_id,
            )
        os.remove(filename)
        return await catevent.delete()
    await catevent.edit(f"{caption} \n\n**OUTPUT:**\n`{text}`")
