# By @yuki
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.phone import CreateGroupCallRequest
from telethon.tl.functions.phone import DiscardGroupCallRequest
from telethon.tl.functions.phone import GetGroupCallRequest
from telethon.tl.functions.phone import InviteToGroupCallRequest
from userbot import catub

plugin_category = "useless"

async def getvc(deep):
    chat_ = await deep.client(GetFullChannelRequest(deep.chat_id))
    _chat = await deep.client(GetGroupCallRequest(chat_.full_chat.call, limit=0))
    return _chat.call

def all_users(a, b):
    for c in range(0, len(a), b):
        yield a[c : c + b]


@catub.cat_cmd(
    pattern="startvc$",
    command=("startvc", plugin_category),
    info={
        "header": "Join voice chat",
        "usage": [
            "{tr}startvc",
        ],
    },
)
async def _(deep):
    "Start voice chat"
    try:
        await deep.client(CreateGroupCallRequest(deep.chat_id))
        await deep.edit("`Voice chat started successfully`")
    except Exception as e:
        await deep.edit( f"`{str(e)}`")

@catub.cat_cmd(
    pattern="endvc$",
    command=("endvc", plugin_category),
    info={
        "header": "End voice chat",
        "usage": [
            "{tr}endvc",
        ],
    },
)
async def _(deep):
    "End voice chat"
    try:
        await bot(DiscardGroupCallRequest(await getvc(deep)))
        await deep.edit("`Voice chat ended successfully`")
    except Exception as e:
        await deep.edit( f"`{str(e)}`")
