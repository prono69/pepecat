# Modified by @kirito6969
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Special credits:
# https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/plugins/webupload.py

import asyncio
import json
import os
import re
import subprocess

import requests
from telethon import functions

from userbot import catub
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "misc"
LOGS = logging.getLogger(__name__)


link_regex = re.compile(
    "((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL
)


@catub.cat_cmd(
    pattern="labstack(?:\s|$)([\s\S]*)",
    command=("labstack", plugin_category),
    info={
        "header": "To upload media to labstack.",
        "description": "Will upload media to labstack and shares you link so that you can share with friends and it expires automatically after 7 days",
        "usage": "{tr}labstack <reply to media or provide path of media>",
    },
)
async def labstack(event):
    "to upload media to labstack"
    editor = await edit_or_reply(event, "Processing...")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if input_str:
        filebase = input_str
    elif reply:
        filebase = await event.client.download_media(
            reply.media, Config.TMP_DOWNLOAD_DIRECTORY
        )
    else:
        return await editor.edit(
            "Reply to a media file or provide a directory to upload the file to labstack"
        )
    filesize = os.path.getsize(filebase)
    filename = os.path.basename(filebase)
    headers2 = {"Up-User-ID": "IZfFbjUcgoo3Ao3m"}
    files2 = {
        "ttl": 604800,
        "files": [{"name": filename, "type": "", "size": filesize}],
    }
    r2 = requests.post(
        "https://up.labstack.com/api/v1/links", json=files2, headers=headers2
    )
    r2json = json.loads(r2.text)
    url = f'https://up.labstack.com/api/v1/links/{r2json["code"]}/send'
    max_days = 7
    command_to_exec = [
        "curl",
        "-F",
        f"files=@{filebase}",
        "-H",
        "Transfer-Encoding: chunked",
        "-H",
        "Up-User-ID: IZfFbjUcgoo3Ao3m",
        url,
    ]

    try:
        t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        LOGS.info("Status : FAIL", exc.returncode, exc.output)
        return await editor.edit(exc.output.decode("UTF-8"))
    else:
        LOGS.info(t_response)
        t_response_arry = (
            f'https://up.labstack.com/api/v1/links/{r2json["code"]}/receive'
        )
    await editor.edit(
        t_response_arry + "\nMax Days:" + str(max_days), link_preview=False
    )


@catub.cat_cmd(
    pattern=r"webupload\s?(.+?)?\s--(fileio|anonfiles|transfer|filebin|anonymousfiles|bayfiles|megaupload|vshare|0x0|ninja|infura)",
    command=("webupload", plugin_category),
    info={
        "header": "To upload media to some online media sharing platforms.",
        "description": "You can upload media to any of the sites mentioned. This helps in sharing links with others.",
        "options": {
            "fileio": "to file.io site",
            "anonfiles": "to anonfiles site",
            "transfer": "to transfer.sh site",
            "filebin": "to file bin site",
            "anonymousfiles": "to anonymousfiles site",
            "bayfiles": "to bayfiles site",
            "megaupload": "To megaupload",
            "vshare": "To Vshare site",
            "0x0": "To 0x0 site",
            "ninja": "To ninja site",
            "infura": "To infura site",
        },
        "usage": [
            "{tr}webupload --option <Reply to media>",
            "{tr}webupload path --option",
        ],
        "examples": "{tr}webupload --fileio reply to media file.",
    },
)
async def _(event):
    "To upload media to some online media sharing platforms"
    editor = await edit_or_reply(event, "Processing ...")
    
    # Capture the input string (file path) and selected transfer option
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    catcheck = None

    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        if not reply or not reply.media:
            return await editor.edit("Please reply to a media file.")
        file_name = await event.client.download_media(
            reply.media, Config.TMP_DOWNLOAD_DIRECTORY
        )
        catcheck = True

    # Command dictionary for various upload services
    CMD_WEB = {
        "fileio": 'curl -F "file=@{full_file_path}" https://file.io',
        "anonfiles": 'curl -F "file=@{full_file_path}" https://api.anonfiles.com/upload',
        "transfer": 'curl --upload-file "{full_file_path}" https://transfer.sh/' + os.path.basename(file_name),
        "filebin": 'curl -X POST --data-binary "@{full_file_path}" -H "filename: {bare_local_name}" "https://filebin.net"',
        "anonymousfiles": 'curl -F "file=@{full_file_path}" https://api.anonymousfiles.io/',
        "vshare": 'curl -F "file=@{full_file_path}" https://api.vshare.is/upload',
        "bayfiles": 'curl -F "file=@{full_file_path}" https://bayfiles.com/api/upload',
        "megaupload": 'curl -F "file=@{full_file_path}" https://megaupload.is/api/upload',
        "0x0": 'curl -F "file=@{full_file_path}" https://0x0.st',
        "ninja": "curl -i -F file=@{full_file_path} https://tmp.ninja/api.php?d=upload-tool",
        "infura": "curl -X POST -F file=@'{full_file_path}' \"https://ipfs.infura.io:5001/api/v0/add?pin=true\"",
    }

    filename = os.path.basename(file_name)

    try:
        selected_one = CMD_WEB[selected_transfer].format(
            full_file_path=file_name, bare_local_name=filename
        )
    except KeyError:
        return await editor.edit("**Invalid selected Transfer option**")

    # Start the subprocess to execute the command
    process = await asyncio.create_subprocess_shell(
        selected_one, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    error = stderr.decode().strip()

    if t_response := stdout.decode().strip():
        try:
            t_response = json.dumps(json.loads(t_response), sort_keys=True, indent=4)
        except Exception as e:
            # Handle non-JSON responses from some sites
            LOGS.info(str(e))
        urls = re.findall(link_regex, t_response)
        result = "**Uploaded File link/links :**\n" + "\n".join(urls) if urls else t_response
        await editor.edit(result)
    else:
        await editor.edit(f"Error: {error}")

    # Remove file if it was downloaded
    if catcheck:
        try:
            os.remove(file_name)
        except Exception as e:
            LOGS.info(f"Error removing file: {str(e)}")


# By @FeelDeD


@catub.cat_cmd(
    pattern="sl",
    command=("sl", plugin_category),
    info={
        "header": "Stream/Download Link Generator",
        "usage": [
            "{tr}sl <reply a file/media>",
        ],
    },
)
async def sl(odi):
    "Stream/Download Link Generator"
    file = await odi.get_reply_message()
    await odi.edit("`Processing ...`")
    if not (file and file.document):
        await edit_delete(odi, "`Please reply a file/media`", 6)
    elif file.sticker:
        await edit_delete(odi, "`Please reply a file/media`", 6)
    elif file.gif:
        await edit_delete(odi, "`Please reply a file/media`", 6)
    else:
        chat = "@TG_FileStreamBot"
        async with odi.client.conversation(chat) as conv:
            try:
                await odi.client(functions.contacts.UnblockRequest(conv.chat_id))
                start = await conv.send_message("/start")
                await conv.get_response()
                end = await conv.send_message(file)
                stream = await conv.get_response()
                await odi.edit(stream.text)
                msgs = []
                for _ in range(start.id, end.id + 2):
                    msgs.append(_)
                await odi.client.delete_messages(conv.chat_id, msgs)
                await odi.client.send_read_acknowledge(conv.chat_id)
            except stream:
                print("Error")
