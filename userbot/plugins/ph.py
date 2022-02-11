# Inline PornHub Search by @kirito6969 for PepeCat

from pornhub_api import PornhubApi
from telethon import Button, events

from userbot import catub

from ..core.decorators import check_owner


@catub.tgbot.on(events.InlineQuery(pattern=r"ph(.*)"))
@check_owner
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    if event.query.user_id != bot.uid:
        resultm = builder.article(
            title="• NIKAL LAWDE •",
            text=f"You Can't Use This Bot. \nDeploy Your Own PEPECAT",
        )
        await event.answer([resultm])
        return
    results = []
    input_str = event.pattern_match.group(1)
    api = PornhubApi()
    data = api.search.search(input_str, ordering="mostviewed")
    ok = 1
    for vid in data.videos:
        if ok <= 5:
            lul_m = f"[𝙋𝙤𝙧𝙣𝙃𝙪𝙗 𝙎𝙚𝙖𝙧𝙘𝙝] \n**Sᴇᴀʀᴄʜ Qᴜᴇʀʏ :** __{input_str}__ \n**Vɪᴅᴇᴏ Tɪᴛʟᴇ :** __{vid.title}__ \n**Vɪᴅᴇᴏ Lɪɴᴋ :** __https://www.pornhub.com/view_video.php?viewkey={vid.video_id}__"
            results.append(
                await event.builder.article(
                    title=vid.title,
                    text=lul_m,
                    buttons=[
                        Button.switch_inline(
                            "𝙎𝙚𝙖𝙧𝙘𝙝 𝘼𝙜𝙖𝙞𝙣", query="ph ", same_peer=True
                        )
                    ],
                )
            )
        else:
            pass
    await event.answer(results)
