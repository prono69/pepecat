#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  UniBorg Telegram UseRBot
#  Copyright (C) 2021 @UniBorg

import asyncio
import os
from datetime import datetime
from time import time

from helpers.utils import get_c_m_message
from telethon.errors import ChannelPrivateError

from . import catub, eor


@catub.cat_cmd(
    pattern="dlc ?(.*)",
    command=("dlc", plugin_category),
    info={
        "header": "To download from telegram link",
        "description": "Will download the link to server .",
        "note": "Useful for protected content",
        "usage": [
            "{tr}dlc <reply>",
        ],
    },
)
async def _e(event):
    sm_ = await eor(event, "...")
    reply = await event.get_reply_message()
    input = event.pattern_match.group(1)
    if not input and reply and reply.text:
        input = reply
    elif not input:
        return await eod(event, "__Gib Telegram Message Link__")
    _c, m_ = get_c_m_message(input.raw_text)
    try:
        _ok_m_ = await event.client.get_messages(entity=_c, ids=m_)
    except ChannelPrivateError:
        await sm_.edit("Channel is private or ID is invalid.")
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    c_time = time()
    start = datetime.now()
    downloaded_file_name = await _ok_m_.download_media(
        Config.TMP_DOWNLOAD_DIRECTORY,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            slitu.progress(d, t, sm_, c_time, "trying to download")
        ),
    )
    end = datetime.now()
    ms = (end - start).seconds
    await sm_.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
