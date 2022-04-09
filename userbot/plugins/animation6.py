import asyncio

from . import catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="unoob$",
    command=("unoob", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}unoob",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(9)
    event = await edit_or_reply(event, "You noob")
    animation_chars = [
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
        "𝐢𝐬",
        "𝐛𝐢𝐠𝐠𝐞𝐬𝐭",
        "𝐧𝐨𝐨𝐛",
        "𝐮𝐧𝐭𝐢𝐥",
        "𝐲𝐨𝐮",
        "𝐚𝐫𝐫𝐢𝐯𝐞",
        "😎",
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞 𝐢𝐬 𝐛𝐢𝐠𝐠𝐞𝐬𝐭 𝐧𝐨𝐨𝐛 𝐮𝐧𝐭𝐢𝐥 𝐲𝐨𝐮 𝐚𝐫𝐫𝐢𝐯𝐞 😎",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@catub.cat_cmd(
    pattern="menoob$",
    command=("menoob", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}menoob",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(9)
    event = await edit_or_reply(event, "Me noob")
    animation_chars = [
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
        "𝐢𝐬",
        "𝐛𝐢𝐠𝐠𝐞𝐬𝐭",
        "𝐧𝐨𝐨𝐛",
        "𝐮𝐧𝐭𝐢𝐥",
        "𝐈",
        "𝐚𝐫𝐫𝐢𝐯𝐞",
        "😎",
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞 𝐢𝐬 𝐛𝐢𝐠𝐠𝐞𝐬𝐭 𝐧𝐨𝐨𝐛 𝐮𝐧𝐭𝐢𝐥 𝐈 𝐚𝐫𝐫𝐢𝐯𝐞 😎",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@catub.cat_cmd(
    pattern="upro$",
    command=("upro", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}upro",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(8)
    event = await edit_or_reply(event, "You pro")
    animation_chars = [
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
        "𝐢𝐬",
        "𝐩𝐫𝐨",
        "𝐮𝐧𝐭𝐢𝐥",
        "𝐲𝐨𝐮",
        "𝐚𝐫𝐫𝐢𝐯𝐞",
        "😎",
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞 𝐢𝐬 𝐩𝐫𝐨 𝐮𝐧𝐭𝐢𝐥 𝐲𝐨𝐮 𝐚𝐫𝐫𝐢𝐯𝐞 😎",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@catub.cat_cmd(
    pattern="mepro$",
    command=("mepro", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}mepro",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(8)
    event = await edit_or_reply(event, "Me pro")
    animation_chars = [
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞",
        "𝐢𝐬",
        "𝐩𝐫𝐨",
        "𝐮𝐧𝐭𝐢𝐥",
        "𝐈",
        "𝐚𝐫𝐫𝐢𝐯𝐞",
        "😎",
        "𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞 𝐢𝐬 𝐩𝐫𝐨 𝐮𝐧𝐭𝐢𝐥 𝐈 𝐚𝐫𝐫𝐢𝐯𝐞 😎",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@catub.cat_cmd(
    pattern="quickheal$",
    command=("quickheal", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}quickheal",
    },
)
async def _(event):
    "animation command"
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Quick heal")
    animation_chars = [
        "`Downloading file..`",
        "`File downloaded...`",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 100%\n█████████████████████████ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nTask : 01 of 01 Files scanned...\n\nResult : No virus found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="sqh$",
    command=("sqh", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}sqh",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Sqh")
    animation_chars = [
        "`Downloading file..`",
        "`File downloaded...`",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 100%\n█████████████████████████ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nTask : 01 of 01 Files scanned...\n\nResult : No virus found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="vquickheal$",
    command=("vquickheal", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}vquickheal",
    },
)
async def _(event):
    "animation command"
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "V quick heal")
    animation_chars = [
        "`Downloading file..`",
        "`File downloaded....`",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nFile scanned... 100%\n█████████████████████████ `",
        "`Quick heal total security checkup\n\n\nSubscription : Pro user\nValid until : 31/12/2099\n\nTask : 01 of 01 Files scanned...\n\nResult : Virus found\nMore Info : Torzan , Spyware , Adware`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="macoc$",
    command=("macoc", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}macoc",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Macos")
    animation_chars = [
        "`Connecting to hackintosh...`",
        "`Initiating hackintosh login`",
        "`Loading hackintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading hackintosh... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading hackintosh... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS : Symbian OS\nCurrent OS : hackintosh`\n\n**My PC Specs :**\n\n **CPU :** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics :** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM :** __32GB DDR4 (2,666MHz)__\n\n**Screen :** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage :** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports :** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity :** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera :** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size :** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="windows$",
    command=("windows", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}windows",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Windows")
    animation_chars = [
        "`Connecting to windows 11...`",
        "`Initiating windows 11 login`",
        "`Loading windows 11... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading windows 11... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading windows 11... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS : Symbian OS\nCurrent OS : Windows 11`\n\n**My PC Specs :**\n\n **CPU :** __3.4GHz ryzen 9 5950x (16-core,32 threads 64MB cache, up to 4.9GHz)__\n\n**Graphics :** __Nvidia GeForce RTX 3090 OC (24GB GDDR6X)__\n\n**RAM :** __64GB DDR4 (4000MHz)__\n\n**Screen :** __17.3-inch, UHD (3840 x 2160) 144Hz Hdr G-Sync__\n\n**Storage :** __512GB nvme gen 4 SSD, 5 TB HDD (7,200 rpm)__\n\n**Ports :** __2 x USB 3.1, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), 2 HDMI2.0, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity :** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera :** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size :** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="linux$",
    command=("linux", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}linux",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Linux")
    animation_chars = [
        "`Connecting to linux...`",
        "`Initiating linux login`",
        "`Loading linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading linux... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading linux... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS : Symbian OS\nCurrent OS : Linux`\n\n**My PC Specs :**\n\n **CPU :** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics :** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM :** __32GB DDR4 (2,666MHz)__\n\n**Screen :** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage :** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports :** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity :** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera :** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size :** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="stock$",
    command=("stock", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}stock",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Stock")
    animation_chars = [
        "`Connecting to symbian OS...`",
        "`Initiating symbian OS login`",
        "`Loading symbian OS... 0%\n█████████████████████████ `",
        "`Loading symbian OS... 3%\n█████████████████████▒▒▒▒ `",
        "`Loading symbian OS... 9%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading symbian OS... 23%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading symbian OS... 39%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading symbian OS... 69%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading symbian OS... 89%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Welcome...\n\nStock OS : Symbian OS\nCurrent OS : Symbian OS`\n\n**My PC Specs :**\n\n **CPU :** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics :** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM :** __32GB DDR4 (2,666MHz)__\n\n**Screen :** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage :** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports :** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity :** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera :** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size :** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@catub.cat_cmd(
    pattern="os$",
    command=("os", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}os",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(7)
    event = await edit_or_reply(event, "OS")
    animation_chars = [
        "`Scanning OS..`",
        "`Scanning OS...`",
        "Current loaded OS : Symbian OS\n\n**To boot other OS , use the following trigger :**\n☑️ `macos`\n☑️ `windows`\n☑️ `linux`\n☑️ `stock`",
        "Current loaded OS : Symbian OS\n\n**To boot other OS , use the following trigger :**\n✅ `macos`\n☑️ `windows`\n☑️ `linux`\n☑️ `stock`",
        "Current loaded OS : Symbian OS\n\n**To boot other OS , use the following trigger :**\n✅ `macos`\n✅ `windows`\n☑️ `linux`\n☑️ `stock`",
        "Current loaded OS : Symbian OS\n\n**To boot other OS , use the following trigger :**\n✅ `macos`\n✅ `windows`\n✅ `linux`\n☑️ `stock`",
        "Current loaded OS : Symbian OS\n\n**To boot other OS , use the following trigger :**\n✅ `macos`\n✅ `windows`\n✅ `linux`\n✅ `stock`\n\nDeveloped by : @catuserbot17",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])
