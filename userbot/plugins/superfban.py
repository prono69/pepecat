import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import superfban_sql_helper as superfban_sql
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@catub.cat_cmd(
    pattern="superfban(?:\s|$)([\s\S]*)",
    command=("superfban", plugin_category),
    info={
        "header": "To super fban user in every group where you are admin",
        "description": "Will super fban the person in every group where you are admin only",
        "usage": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def catsuperfban(event):  # sourcery no-metrics
    "To super fban user in every group where you are admin"
    cate = await edit_or_reply(event, "`Super fbanning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`Why would I ban myself ?`")
    if superfban_sql.is_superfbanned(user.id):
        await cate.edit(
            f"`The `[user](tg://user?id={user.id})` is already in gbanned list any way checking again`"
        )
    else:
        superfban_sql.catsuperfban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`You are not admin of atleast one group` ")
    await cate.edit(
        f"`Initiating super fban of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For banning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was super fbanned in {count} groups in {cattaken} seconds`\n\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was super fbanned in {count} groups in {cattaken} seconds`"
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"SFBAN\
                \nSuper fban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**Id : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \nBanned in {count} groups\
                \n**Time taken : **`{cattaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"SFBAN\
                \nSuper fban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**Id : **`{user.id}`\
                \nBanned in {count} groups\
                \n**Time taken : **`{cattaken} seconds`",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@catub.cat_cmd(
    pattern="unsuperfban(?:\s|$)([\s\S]*)",
    command=("unsuperfban", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin",
        "description": "Will unban and also remove from your gbanned list",
        "usage": "{tr}ungban <username/reply/userid>",
    },
)
async def catsuperfban(event):
    "To unban the person from every group where you are admin"
    cate = await edit_or_reply(event, "`Unsuperfbanning...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if superfban_sql.is_superfbanned(user.id):
        superfban_sql.catunsuperfban(user.id)
    else:
        return await edit_delete(
            cate, f"The [user](tg://user?id={user.id}) `is not in your super fbanned list`"
        )
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`You are not even admin of atleast one group `")
    await cate.edit(
        f"Initiating unsuper fban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For unbanning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}`) was unsuperfbanned in {count} groups in {cattaken} seconds`\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was unsuperfbanned in {count} groups in {cattaken} seconds`"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"UNSFBAN\
                \nUnsuper fban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**Id : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \nUnbanned in {count} groups\
                \n**Time taken : **`{cattaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"UNSFBAN\
                \nUnsuper fban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**Id : **`{user.id}`\
                \nUnbanned in {count} groups\
                \n**Time taken : **`{cattaken} seconds`",
            )


@catub.cat_cmd(
    pattern="listsuperfban$",
    command=("listsuperfban", plugin_category),
    info={
        "header": "Shows you the list of all superfbanned users by you",
        "usage": "{tr}listsuperfban",
    },
)
async def gablist(event):
    "Shows you the list of all superfbanned users by you"
    superfbanned_users = superfban_sql.get_all_superfbanned()
    SUPERFBANNED_LIST = "Current super fbanned users\n"
    if len(superfbanned_users) > 0:
        for a_user in superfbanned_users:
            if a_user.reason:
                SUPERFBANNED_LIST += f"[{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                SUPERFBANNED_LIST += (
                    f"[{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason none\n"
                )
    else:
        GBANNED_LIST = "No superfbanned users ( yet )"
    await edit_or_reply(event, SUPERFBANNED_LIST)
