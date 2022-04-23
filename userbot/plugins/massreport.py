# By @yuki

from userbot import catub
from ..core.managers import edit_or_reply
import time

plugin_category = "admin"

@catub.cat_cmd(
    pattern="massreport ?(.*)",
    command=("massreport",
    plugin_category),
      info={
        "header": "Mass reports the user",
        "usage": "{tr}massreport <username/reply>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    cate = await edit_or_reply(event, "`Mass reporting...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`Why would I mass report myself ?`")
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"`the `[user](tg://user?id={user.id})` is already in mass report list any way checking again`"
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`You are not admin of atleast one group` ")
    await cate.edit(
        f"`Initiating mass report of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
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
            f"[{user.first_name}](tg://user?id={user.id}) `was mass reported in {cattaken} seconds`\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was mass reported in {cattaken} seconds`"
        )
