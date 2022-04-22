import os
from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import convert_tosticker, media_type, process

plugin_category = "fun"

@catub.cat_cmd(
    pattern="fq ([\s\S]*)$",
    command=("fq", plugin_category),
    info={
        "header": "Makes your message as sticker quote but with someone else's name",
        "usage": [
            "{tr}fq <username> <message>",
            "{tr}fq message <reply to a person>"
        ],
        "examples": [
            "{tr}fq @missrose_bot Hey",
            "{tr}fq Hey <reply to rose>"
        ],
        "Notes": [
            "• It doesn't work in pms\n"
            "• The user must be part of the group you used the command in"    
        ],
    },
)
async def stickerchat(catquotes):
    "Makes your message as sticker quote framing someone else"
    username = (catquotes.pattern_match.group(1)).split(" ")[0]
    reply = await catquotes.get_reply_message()
    
    if catquotes.is_private: return await edit_delete(catquotes, "`This command doesn't work in pm`")
    
    try: username = int(username)
    except: pass

    try: user = await catquotes.client.get_entity(username) ; for_arg = True ; for_reply = False
    except ValueError:
        if catquotes.reply_to: for_reply = True ; for_arg = False
        else: return await edit_delete(catquotes, "`Please provide a correct username or id of the person`")


    if for_reply:
        message = catquotes.pattern_match.group(1)
        user = (
            await catquotes.client.get_entity(reply.forward.sender)
            if reply.fwd_from
            else reply.sender
        )
        catevent = await edit_or_reply(catquotes, "`Making quote...`")       
        res, catmsg = await process(message, user, catquotes.client, catquotes, None)
    
    if for_arg:
        message = catquotes.pattern_match.group(1)[len(username)+1:]
        catevent = await edit_or_reply(catquotes, "`Making quote...`")
        res, catmsg = await process(message, user, catquotes.client, catquotes, None)

    
    if not res: return
    outfi = os.path.join("./temp", "sticker.png")
    catmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await catquotes.client.send_file(catquotes.chat_id, endfi, reply_to=reply)
    await catevent.delete()
    os.remove(endfi)
