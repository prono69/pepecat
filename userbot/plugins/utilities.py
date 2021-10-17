# By @kirito6969
# Some things are kanged from Ultroid

import asyncio
import calendar
import random
import re
from datetime import datetime as dt
from datetime import timedelta

import pytz
import requests
from bs4 import BeautifulSoup as bs
from telethon import functions
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..helpers.functions import async_searcher
from . import catub, edit_delete, edit_or_reply, mention

plugin_category = "utils"
GBOT = "@HowGayBot"
_copied_msg = {}


@catub.cat_cmd(
    pattern="date$",
    command=("date", plugin_category),
    info={
        "header": "To know current Date and Time",
        "usage": "{tr}date",
    },
)
async def date(event):
    m = dt.now().month
    y = dt.now().year
    d = dt.now().strftime("Date - %B %d, %Y\nTime- %H:%M:%S")
    k = calendar.month(y, m)
    ultroid = await edit_or_reply(event, f"`{k}\n\n{d}`")


# t.me/realnub and t.me/lal_bakthan
@catub.cat_cmd(
    pattern="timer(?:\s|$)([\s\S]*)",
    command=("timer", plugin_category),
    info={
        "header": "timer, try yourself",
        "note": "May not be accurate, especially for DC 5 users.",
        "description": "Timer like in clock, counts till 0 from given seconds.",
        "usage": "{tr}timer <seconds>",
    },
)
async def _(event):
    "Timer like in clock, counts till 0 from given seconds."
    if event.fwd_from:
        return
    try:
        total = event.pattern_match.group(1)
        if not total:
            await edit_delete(event, f"**Usage:** `{tr}timer <seconds>`", 10)
            return
        t = int(total)
        pluto = await edit_or_reply(event, "**Starting...**")
        while t >= 0:
            x = 3 if t > 300 else 1
            try:
                timer = timedelta(seconds=t)
                czy = str(timer).split(".")[0]
                await pluto.edit(czy)
                await asyncio.sleep(x - 0.03)
                t -= x
            except FloodWaitError as e:
                t -= e.seconds
                await asyncio.sleep(e.seconds)
        await pluto.edit(f"**⏱ Time Up!\n⌛️ Time: {total} seconds.**")
    except Exception as e:
        await edit_delete(event, f"`{e}`", 7)


@catub.cat_cmd(
    pattern="gey(?:\s|$)([\s\S]*)",
    command=("gey", plugin_category),
    info={
        "header": "Try yourself!",
        "description": "Try yourself!",
        "usage": "{tr}gey <name>.",
    },
)
async def app_search(event):
    "try yourself"
    name = event.pattern_match.group(1)
    if not name:
        name = " "
    event = await edit_or_reply(event, "`Calculating!..`")
    id = await reply_id(event)
    try:
        score = await event.client.inline_query(GBOT, name)
        await score[0].click(event.chat_id, reply_to=id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit(str(err))


@catub.cat_cmd(
    pattern="cid(?:\s|$)([\s\S]*)",
    command=("cid", plugin_category),
    info={
        "header": "To search a phone number in Truecaller",
        "description": "Searches the given number in the truecaller and provides the details.",
        "usage": "{tr}cid <phone>",
    },
)
async def _(event):
    "To search a phone number in Truecaller"
    args = event.pattern_match.group(1)
    if not args:
        await edit_or_reply(event, f"**Usage:** `{tr}cid <number>`")
        return
    pluto = await edit_or_reply(event, "**__Fetching details...__**")
    chat = "@RespawnRobot"
    await reply_id(event)
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(args)
            check = await conv.get_response()
            replace = check.text
            info = replace.replace(chat, f"{mention}")
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest(chat))
            await edit_delete(
                pluto,
                f"__**An error occurred. Please try again!\n☞**__ `{tr}cid {args}`",
                10,
            )
            return
        await pluto.edit(info)
    await event.client.delete_dialog(chat)


@catub.cat_cmd(
    pattern="mcq ?(.*)",
    command=("mcq", plugin_category),
    info={
        "header": "Chooses a random item in the given options, give a comma ',' to add multiple option",
        "usage": ["{tr}mcq <options>", "{tr}mcq a,b,c,d", "{tr}mcq cat,dog,life,death"],
    },
)
async def mcq(event):
    "Chooses a random item in the given options, give a comma ',' to add multiple option"
    osho = event.pattern_match.group(1)
    if not osho:
        return await edit_delete(event, "`What to choose from`", 10)
    options = osho.split(",")
    await event.edit(f"**Input:** `{osho}`\n**Random:** `{random.choice(options)}`")


@catub.cat_cmd(
    pattern="eod(?:\s|$)([\s\S]*)",
    command=("eod", plugin_category),
    info={
        "header": "Get Events of the day.",
        "description": "Get Events of the day.",
        "usage": "{tr}eod\n{tr}eod <dd/mm>",
    },
)
async def diela(e):
    match = e.pattern_match.group(1)
    m = await edit_or_reply(e, "`Processing...`")
    li = "https://daysoftheyear.com"
    te = "🎊 **Events of the Day**\n\n"
    if match:
        date = match.split("/")[0]
        month = match.split("/")[1]
        li += "/days/2021/" + month + "/" + date
        te = "• **Events for {}/2021**\n\n".format(match)
    else:
        da = dt.today().strftime("%F").split("-")
        li += "/days/2021/" + da[1] + "/" + da[2]
    ct = requests.get(li).content
    bt = bs(ct, "html.parser", from_encoding="utf-8")
    ml = bt.find_all("a", "js-link-target", href=re.compile("daysoftheyear.com/days"))
    for eve in ml[:5]:
        te += "• " + f'[{eve.text}]({eve["href"]})\n'
    await m.edit(te, link_preview=False)


@catub.cat_cmd(
    pattern="cpy$",
    command=("cpy", plugin_category),
    info={
        "header": "Copy the replied message, with formatting. Expires in 24hrs.",
        "usage": "{tr}cpy <reply to a message>",
    },
)
async def copp(event):
    msg = await event.get_reply_message()
    if not msg:
        return await edit_delete(event, f"Use `{tr}cpy` as reply to a message!", 5)
    _copied_msg["CLIPBOARD"] = msg
    await edit_delete(event, f"Copied. Use `{tr}pst` to paste!", 10)


@catub.cat_cmd(
    pattern="pst$",
    command=("pst", plugin_category),
    info={
        "header": "Paste the copied message, with formatting.",
        "usage": "{tr}pst",
    },
)
async def colgate(event):
    await toothpaste(event)


async def toothpaste(event):
    try:
        await event.respond(_copied_msg["CLIPBOARD"])
        try:
            await event.delete()
        except BaseException:
            pass
    except KeyError:
        return await edit_delete(
            event,
            f"Nothing was copied! Use `{tr}cpy` as reply to a message first!",
        )
    except Exception as ex:
        return await edit_delete(event, str(ex), 5)


@catub.cat_cmd(
    pattern="dob(?:\s|$)([\s\S]*)",
    command=("dob", plugin_category),
    info={
        "header": "Put in dd/mm/yy Format only.",
        "usage": "{tr}dob <dd/mm/yy>",
        "examples": "{tr}dob 01/01/1999",
    },
)
async def hbd(event):
    if not event.pattern_match.group(1):
        return await edit_delete(event, "`Put input in dd/mm/yyyy format`")
    if event.reply_to_msg_id:
        kk = await event.get_reply_message()
        nam = await event.client.get_entity(kk.from_id)
        name = nam.first_name
    else:
        name = catub.me.first_name
    zn = pytz.timezone("Asia/Kolkata")
    abhi = dt.now(zn)
    n = event.text
    q = n[5:]
    kk = q.split("/")
    p = kk[0]
    r = kk[1]
    s = kk[2]
    day = int(p)
    month = r
    paida = q
    try:
        jn = dt.strptime(paida, "%d/%m/%Y")
    except BaseException:
        return await edit_delete(event, "`Put input in dd/mm/yyyy format`")
    jnm = zn.localize(jn)
    zinda = abhi - jnm
    barsh = (zinda.total_seconds()) / (365.242 * 24 * 3600)
    saal = int(barsh)
    mash = (barsh - saal) * 12
    mahina = int(mash)
    divas = (mash - mahina) * (365.242 / 12)
    din = int(divas)
    samay = (divas - din) * 24
    ghanta = int(samay)
    pehl = (samay - ghanta) * 60
    mi = int(pehl)
    sec = (pehl - mi) * 60
    slive = int(sec)
    y = int(s) + int(saal) + 1
    m = int(r)
    brth = dt(y, m, day)
    cm = dt(abhi.year, brth.month, brth.day)
    ish = (cm - abhi.today()).days + 1
    dan = ish
    if dan == 0:
        hp = "`Happy BirthDay To U🎉🎊`"
    elif dan < 0:
        okk = 365 + ish
        hp = f"{okk} Days Left 🥳"
    elif dan > 0:
        hp = f"{ish} Days Left 🥳"
    if month == "12":
        sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == "01":
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == "02":
        sign = "Aquarius" if (day < 19) else "Pisces"
    elif month == "03":
        sign = "Pisces" if (day < 21) else "Aries"
    elif month == "04":
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == "05":
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month == "06":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "07":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "08":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "09":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "10":
        sign = "Libra" if (day < 23) else "Scorpion"
    elif month == "11":
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    sign = f"{sign}"
    params = (("sign", sign), ("today", day))
    json = await async_searcher(
        "https://aztro.sameerkumar.website/", post=True, params=params, re_json=True
    )
    dd = json.get("current_date")
    ds = json.get("description")
    lt = json.get("lucky_time")
    md = json.get("mood")
    cl = json.get("color")
    ln = json.get("lucky_number")
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"""
    Name -: {name}

D.O.B -:  {paida}

Lived -:  {saal}yr, {mahina}m, {din}d, {ghanta}hr, {mi}min, {slive}sec

Birthday -: {hp}

Zodiac -: {sign}

**Horoscope On {dd} -**

`{ds}`

    Lucky Time :-        {lt}
    Lucky Number :-   {ln}
    Lucky Color :-        {cl}
    Mood :-                   {md}
    """,
        reply_to=event.reply_to_msg_id,
    )
