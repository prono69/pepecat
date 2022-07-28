# Modified open by @DazaiSun
import os
from re import sub

from quotefancy import get_quote
from requests import get
from telethon.errors import ChatSendMediaForbiddenError

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _catutils, reply_id
from ..sql_helper.globals import gvarstatus
from . import catub

plugin_category = "misc"
opn = []


@catub.cat_cmd(
    pattern="open",
    command=("open", plugin_category),
    info={
        "header": "Reveal documents.",
        "usage": "{tr}open <reply to document>",
    },
)
async def _(event):
    xx = await edit_or_reply(event, "`Loading ...`")
    if not event.reply_to_msg_id:
        return await edit_or_reply(xx, "Reply to a readable file", time=10)
    a = await event.get_reply_message()
    if not a.media:
        return await edit_or_reply(xx, "Reply to a readable file", time=10)
    b = await a.download_media()
    with open(b, "r") as c:
        d = c.read()
    n = 4096
    for bkl in range(0, len(d), n):
        opn.append(d[bkl : bkl + n])
    for bc in opn:
        await event.client.send_message(
            event.chat_id,
            f"`{bc}`",
            reply_to=event.reply_to_msg_id,
        )
    await event.delete()
    opn.clear()
    os.remove(b)
    await xx.delete()


@catub.cat_cmd(
    pattern="gstat ?(.*)",
    command=("gstat", plugin_category),
    info={
        "header": "Check group status.",
        "usage": "{tr}gstat <group name>",
    },
)
async def get_stats(event):
    chat = event.pattern_match.group(1)
    try:
        stats = await event.client.get_stats(chat)
    except:
        await edit_or_reply(
            event,
            "Failed to get stats for the current chat, Make sure you are **admin** and chat has more than **500 members**.",
        )
        return
    min_time = stats.period.min_date.strftime("From %d/%m/%Y, %H:%M:%S")
    max_time = stats.period.max_date.strftime("To %d/%m/%Y, %H:%M:%S")
    member_count = int(stats.members.current) - int(stats.members.previous)
    message_count = int(stats.messages.current) - int(stats.messages.previous)
    msg = f"Group stats:\n{min_time} {max_time}\nMembers count increased by {member_count}\nMessage count increased by {message_count}"
    await edit_or_reply(event, msg)


@catub.cat_cmd(
    pattern="ips ?(.*)",
    command=("ips", plugin_category),
    info={
        "header": "Find information about an IP address",
        "usage": "{tr}ips <ip address>",
    },
)
async def ipcmd(event):
    """Use as .ips <ip> (optional)"""
    ip = event.pattern_match.group(1)
    if not ip:
        await edit_delete(event, "`Give me an ip address :(`")

    lookup = get(f"http://ip-api.com/json/{ip}").json()
    fixed_lookup = {}

    for key, value in lookup.items():
        special = {
            "lat": "Latitude",
            "lon": "Longitude",
            "isp": "ISP",
            "as": "AS",
            "asname": "AS name",
        }
        if key in special:
            fixed_lookup[special[key]] = str(value)
            continue

        key = sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", key)
        key = key.capitalize()

        if not value:
            value = "None"

        fixed_lookup[key] = str(value)

    text = ""

    for key, value in fixed_lookup.items():
        text = text + f"<b>{key}:</b> <code>{value}</code>\n"

    await edit_or_reply(
        event, f"<b>IP Information of {ip}</b>\n\n{text}", parse_mode="html"
    )


@catub.cat_cmd(
    pattern="totalmsgs ?(.*)",
    command=("totalmsgs", plugin_category),
    info={
        "header": "Returns your or any user's total msg count in current chat",
        "usage": "{tr}totalmsgs [username]/<reply>/nothing",
    },
)
async def _(e):
    match = e.pattern_match.group(1)
    if match:
        user = match
    elif e.is_reply:
        user = (await e.get_reply_message()).sender_id
    else:
        user = "me"
    a = await e.client.get_messages(e.chat_id, 0, from_user=user)
    user = await e.client.get_entity(user)
    await edit_or_reply(e, f"Total msgs of `{user.first_name}`\n**Here :** `{a.total}`")


@catub.cat_cmd(
    pattern="qfancy ?(.*)",
    command=("qfancy", plugin_category),
    info={
        "header": "Gets random quotes from QuoteFancy.com.",
        "usage": "{tr}qfancy",
    },
)
async def quotefancy(e):
    mes = await edit_or_reply(e, "`Processing...`")
    reply = await reply_id(e)
    img = get_quote("img", download=True)
    try:
        await e.client.send_file(e.chat_id, img, reply_to=reply)
        os.remove(img)
        await mes.delete()
    except ChatSendMediaForbiddenError:
        quote = get_quote("text")
        await edit_or_reply(e, f"`{quote}`")
    except Exception as e:
        await edit_delete(e, f"**ERROR** - {str(e)}")


# By @FeelDed


@catub.cat_cmd(
    pattern="mdl ?(.*)",
    command=("mdl", plugin_category),
    info={
        "header": "Movie downloader by @FeelDeD",
        "usage": [
            "{tr}mdl <movie name>",
        ],
    },
)
async def mdl(odi):
    "Movie DL By @FeelDeD"
    if odi.fwd_from:
        return
    bot = gvarstatus("INLINE_BOT") or "@ProSearchBot"
    text = odi.pattern_match.group(1)
    reply_to_id = await reply_id(odi)
    if not text:
        await edit_delete(odi, "`Give me a movie/serial name`", 5)
    else:
        await odi.edit("`Processing ...`")
        run = await odi.client.inline_query(bot, text)
        if not run:
            await edit_delete(odi, "`No result found`", 5)
        else:
            await odi.delete()
            result = await run[0].click("me")
            await odi.client.send_file(
                odi.chat_id, result, reply_to=reply_to_id, caption=False
            )
            await result.delete()


# By t.me/feelded


@catub.cat_cmd(
    pattern="embed ?(.*)",
    command=("embed", plugin_category),
    info={
        "header": "Easily find and embed company logos",
        "examples": "{tr}embed spotify.com",
        "usage": [
            "{tr}embed <site link>",
        ],
    },
)
async def embed(odi):
    "Embed company logos"
    try:
        reply_to_id = await reply_id(odi)
        link = odi.pattern_match.group(1)
        if not link:
            await edit_delete(odi, "`Give a company site link`", 6)
        elif "http" in link:
            await edit_delete(
                odi, "`Use true structure(Without https://)`\n`.embed python.com` ", 10
            )
        else:
            await odi.edit("`Processing ...`")
            up = await odi.client.send_file(
                odi.chat_id,
                f"http://logo.clearbit.com/{link}",
                reply_to=reply_to_id,
                caption=f"**Query:** {link}",
            )
            await odi.delete()
    except Exception:
        await edit_delete(
            odi, "`No result found`\n`Try another link with true structure`"
        )


# By @FeelDeD


@catub.cat_cmd(
    pattern="pip(.*)",
    command=("pip", plugin_category),
    info={
        "header": "Run pip",
        "examples": "{tr}pip show telethon",
        "usage": [
            "{tr}pip <code>",
        ],
    },
)
async def movie(event):
    "Run pip"
    await event.edit("`Processing ...`")
    code = event.pattern_match.group(1)
    cmd = f"pip {code}"
    run = (await _catutils.runcmd(cmd))[0]
    await event.edit(f"<b>Results:</b>\n\n<code>{run}</code>", parse_mode="html")
