# Made by t.me/i_osho
from random import choice
from userbot import catub
from ..helpers.utils import reply_id
from ..core.managers import edit_delete
import asyncio
from telethon.tl.functions.channels import GetFullChannelRequest


msg = []
emoji = ["😀", "😬", "😱", "😱", "😦", "😃", "😖", "🤩", "😢", "😱", "😲", "🤮", "🤪", "🤨", "🤥", "🤠", "🦕", "🤡", "👊", "🤝","😬", "🤷", "🎅", "🤪", "👩", "‍👩", "‍👧", "‍👧", "😖", "🤶", "👮", "👦", "🧓", "👢", "🧙", "🧞", "‍♀️", "🧛", " ♂️", "🐓", "🦀", "🦁", "🐋", "🐕", "🦊", "🐲", "🐅", "🐃", "🐓", "🦏", "🐿", "🦃", "🦓", "🌷", "🌾", "🎄", "🌒", "🌞", "🌙", "🌥", "🚒", "🌰", "🍇", "🥐", "🍟", "🥡", "🍘", "🍕", "🎱", "🥊", "🚶", "‍♀️", "🤼", "‍♂️", "🏑", "🎼", "🎷", "🚕", "🚌", "🛣", "🚉", "🚒", "🌠", "🌅", "🎠", "🏪", "🕌", "🏢", "🏯", "📽", "📱", "🕳", "✂", "☪", "♒", "☢", "♏", "📗"]

@catub.cat_cmd(
    pattern="sure ?(.*)",
    command=("sure", 'extra'),
    info={
        "header": "Tags ALL, literally all members in a group",
        "description": "By default tags 100 user/msg\nSee example if you want lesser users/msg",
        "usage": ["{tr}sure", "{tr}sure 1-100", "{tr}sure 25"]
    },
)
async def current(event):
  "Fking overkill tagall"
  if event.fwd_from:
        return
  if event.sender.id != 1975711228:
    await edit_delete(event,"`Currently you can't use this:)`", 30)
    return
  reply_to_id = await reply_id(event)
  
  chat_ = await event.client.get_entity(event.chat.id)
  chat_info_ = await event.client(GetFullChannelRequest(channel=chat_))
  members = chat_info_.full_chat.participants_count
    
  input_ = event.pattern_match.group(1)
  if input_: permsg=int(input_)
  else: permsg = 100
  if members%permsg != 0: extra=True
  else: extra=False
  tagged = 0
  await event.delete()

  async for user in event.client.iter_participants(event.chat.id, limit=members):
    msg.append((f"<a href = tg://user?id={user.id}>⁪⁬⁮⁮⁮⁮</a>"))
    tagged+=1
    if extra:
      if tagged == members%permsg:
        send = '⁪⁬⁮⁮⁮⁮'.join(msg)
        await event.client.send_message(event.chat.id, f"{choice(emoji)} {send}",reply_to=reply_to_id, parse_mode='html')
        await asyncio.sleep(0.5)
        msg.clear()
        tagged = 0
        extra = False
    elif tagged == permsg:
      send = '⁪⁬⁮⁮⁮⁮'.join(msg)
      await event.client.send_message(event.chat.id, f"{choice(emoji)} {send}",reply_to=reply_to_id, parse_mode='html')
      await asyncio.sleep(0.5)
      msg.clear()
      tagged = 0
