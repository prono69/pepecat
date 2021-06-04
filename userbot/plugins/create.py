from telethon.errors import BadRequestError
from telethon.tl import functions
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from ..Config import Config
from . import catub, edit_or_reply

plugin_category = "tools"


@catub.cat_cmd(
    pattern="create (b|g|c) (.*)",
    command=("create", plugin_category),
    info={
        "header": "To create a private group/channel with userbot.",
        "description": "Use this cmd to create super group , normal group or channel.",
        "flags": {
            "b": "to create a private super group",
            "g": "To create a private basic group.",
            "c": "to create a private channel",
        },
        "usage": "{tr}create (b|g|c) <name of group/channel>",
        "examples": "{tr}create b catuserbot",
    },
)
async def _(event):
    "To create a private group/channel with userbot"
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "c":
        descript = "This is a Test Channel created using catuserbot"
    else:
        descript = "This is a Test Group created using catuserbot"
    event = await edit_or_reply(event, "creating......")
    flag = False
    if type_of_group == "b":
        try:
            new_rights = ChatAdminRights(
                add_admins=False,
                invite_users=True,
                change_info=False,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
            )
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.TG_BOT_USERNAME],
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Group `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
            flag = True
            try:
                rank = "admin"
                p = await event.client.get_entity(Config.TG_BOT_USERNAME)
                result = await event.client(
                    EditAdminRequest(created_chat_id, p.id, new_rights, rank)
                )
            except BadRequestError:
                pass
        except Exception as e:
            if not flag:
                await event.edit(str(e))
            else:
                LOGS.error(e)
    elif type_of_group in ["g", "c"]:
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=type_of_group != "c",
                )
            )

            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Channel `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:
            await event.edit(str(e))
    else:
        await event.edit("Read `.help create` to know how to use me")


@catub.cat_cmd(
    pattern="shift (.*)",
    command=("shift", plugin_category),
    info={
        "header": "BEWARE DANGER AHEAD",
        "description": "To copy all messages/files from a channel/group to your channel/group",
        "usage": "{tr}shift <id of source group/channel> | <id of destination group/channel>",
        "examples": "{tr}shift -100|-100",
    },
)
async def _(e):
    x = e.pattern_match.group(1)
    z = await edit_or_reply(e, "`processing..`")
    a, b = x.split("|")
    try:
        c = int(a)
    except Exception:
        try:
            c = (await bot.get_entity(a)).id
        except Exception:
            await z.edit("invalid Channel given")
            return
    try:
        d = int(b)
    except Exception:
        try:
            d = (await bot.get_entity(b)).id
        except Exception:
            await z.edit("invalid Channel given")
            return
    async for msg in bot.iter_messages(int(c), reverse=True):
        try:
            await asyncio.sleep(1.5)
            await bot.send_message(int(d), msg)
        except BaseException:
            pass
    await z.edit("Done")
