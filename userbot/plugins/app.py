"""
Fetch App Details from Playstore.
.app <app_name> to fetch app details.
  © [cHAuHaN](http://t.me/amnd33p)
"""

import bs4
import requests

from . import ALIVE_NAME, catub, edit_or_reply, edit_delete, reply_id

plugin_category = "utils"


@catub.cat_cmd(
    pattern="app ([\s\S]*)",
    command=("app", plugin_category),
    info={
        "header": "To search any app in playstore",
        "description": "Searches the app in the playstore and provides the link to the app in playstore and fetchs app details",
        "usage": "{tr}app <name>",
    },
)
async def app_search(event):
    "To search any app in playstore."
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "`Searching!..`")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += f"\n\n===> {ALIVE_NAME} <==="
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))

        
@catub.cat_cmd(
    pattern="iapp(?:\s|$)([\s\S]*)",
    command=("iapp", plugin_category),
    info={
        "header": "To search any app in playstore via inline.",
        "description": "Searches the app in the playstore and provides the link to the app in playstore and fetches app details via inline.",
        "usage": "{tr}iapp <name>",
    },
)
async def app_search(event):
    "To search any app in playstore via inline."
    app_name = event.pattern_match.group(1)
    if not app_name:
        await edit_delete(event, f"**Usage:** `{tr}iapp <name>`", 10)
        return
    reply_to_id = await reply_id(event)
    APPBOT = "@nedzbot"
    cozyneko = "app" + app_name
    event = await edit_or_reply(event, "`Searching!..`")
    try:
        score = await event.client.inline_query(APPBOT, cozyneko)
        await score[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))
        
        
@catub.cat_cmd(
    pattern="sapp ?(.*)",
    command=("sapp", plugin_category),
    info={
        "header": "App dLink plugin",
        "usage": [
            "{tr}sapp <app name>",
        ],
    },
)
async def app(event):
    if event.fwd_from:
        return
    await event.edit("`Processing ...`")
    bot = "apkdl_bot"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not text:
        return await edit_delete(
            event, "Give a app name"
        )
    run = await event.client.inline_query(bot, text)
    result = await run[0].click(Config.PRIVATE_GROUP_BOT_API_ID)
    await result.delete()
    await event.client.send_message(event.chat_id, result, reply_to=reply_to_id)
    await event.delete()        