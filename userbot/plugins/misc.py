from . import catub
from ..core.managers import edit_or_reply

plugin_category = "utils"


@catub.cat_cmd(
    pattern="pm ?(.*)",
    command=("pm", plugin_category),
    info={
        "header": "DM a hooman",
        "usage": "{tr}pm <text>|<username>",
    },
)
async def _(cat):
    kk = cat.pattern_match.group(1)
    a = await edit_or_reply(cat, "`Sending Message...`")
    replied = await cat.get_reply_message()
    query = kk
    if replied:
        text = replied.message
        username = query
    elif "|" in query:
        text, username = query.split("|")

    await bot.send_message(f"{username}", f"{text}")
    await a.edit("`Done`")
    await sleep(2)
    await a.delete()


@catub.cat_cmd(
    pattern="reveal",
    command=("reveal", plugin_category),
    info={
        "header": "Reveal documents.",
        "usage": "{tr}reveal <reply to document>",
    },
)
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await edit_or_reply(event, "**Reading file...**")
    if len(c) > 4095:
        await a.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    remove(b)


@catub.cat_cmd(
    pattern="gstat",
    command=("gstat", plugin_category),
    info={
        "header": "Check group status.",
        "usage": "{tr}gstat",
    },
)
async def get_stats(event):
    chat = event.text.split(" ", 1)[1]
    try:
        stats = await bot.get_stats(chat)
    except:
        await edit_or_reply(event,
            "Failed to get stats for the current chat, Make sure you are **admin** and chat has more than **500 members**."
        )
        return
    min_time = stats.period.min_date.strftime("From %d/%m/%Y, %H:%M:%S")
    max_time = stats.period.max_date.strftime("To %d/%m/%Y, %H:%M:%S")
    member_count = int(stats.members.current) - int(stats.members.previous)
    message_count = int(stats.messages.current) - int(stats.messages.previous)
    msg = f"Group stats:\n{min_time} {max_time}\nMembers count increased by {member_count}\nMessage count increased by {message_count}"
    await edit_or_reply(event, msg)

    
@catub.cat_cmd(
    pattern="dm ?(.*)",
    command=("dm", plugin_category),
    info={
        "header": "DM a hooman",
        "usage": [
            "{tr}dm <username>|<text>",
            "{tr}dm <text>|<reply>",
        ],
    },
)
async def _(dc):

    d = dc.pattern_match.group(1)

    c = d.split("|")

    chat_id = c[0]
    try:
        chat_id = int(chat_id)

    except BaseException:

        pass

    msg = ""
    masg = await dc.get_reply_message()
    if dc.reply_to_msg_id:
        await bot.send_message(chat_id, masg)
        await dc.edit(f"**{MASTER}:** Your message was successfully delivered")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await edit_or_reply(dc, f"**{MASTER}:** Your message was successfully delivered")
    except BaseException:
        await edit_or_reply(dc, ".dm (username)|(text)")    