import requests

pawn = [
    "nsfw",
    "nsfw_gifs",
    "nsfw_gif",
    "realgirls",
    "porn",
    "porn_gifs",
    "porninfifteenseconds",
    "CuteModeSlutMode",
    "NSFW_HTML5",
    "besthqporngifs",
    "boobs",
    "pussy",
    "jigglefuck",
    "GirlsFinishingTheJob",
    "SheLikesItRough",
    "dirtysmall",
    "NsfwGifsMonster",
    "RedheadGifs",
    "IndianPorn",
    "DesiBoners",
    "IndianBabes",
    "Mmsvideos",
    "snapleaks",
    "creampie",
    "creampies",
    "workgonewild",
    "militarygonewild",
    "BustyPetite",
    "cumsluts",
    "HappyEmbarrassedGirls",
    "suicidegirls",
    "porninaminute",
    "SexInFrontOfOthers",
    "tiktoknsfw",
    "tiktokporn",
    "TikThots",
    "NSFWFunny",
    "GWNerdy",
    "WatchItForThePlot",
    "HoldTheMoan",
    "OnOff",
    "TittyDrop",
    "extramile",
    "adorableporn",
]

endpoints = {
    "v1": {
        "end": [
            "pussy",
            "cum",
            "boobs",
            "bj",
            "anal",
            "hentai",
            "feet",
            "blowjob",
            "poke",
            "holo",
            "baka",
        ],
        "api": "http://api.nekos.fun:8080/api/",
        "checker": "image",
    },
    "v2": {
        "end": [
            "lewd",
            "spank",
            "gasm",
            "tickle",
            "slap",
            "pat",
            "neko",
            "meow",
            "lizard",
            "kiss",
            "hug",
            "fox_girl",
            "feed",
            "cuddle",
            "ngif",
            "smug",
            "woof",
            "wallpaper",
            "goose",
            "gecg",
            "avatar",
            "waifu",
        ],
        "api": "https://nekos.life/api/v2/img/",
        "checker": "url",
    },
    "v3": {
        "end": [
            "ass",
            "anal",
            "ahegao",
            "bite",
            "boobs",
            "bdsm",
            "boobjob",
            "blowjob",
            "creampie",
            "cuckold",
            "classic",
            "depression",
            "elves",
            "ero",
            "femdom",
            "footjob",
            "gangbang",
            "glasses",
            "gif",
            "hentai",
            "handjob",
            "incest",
            "jahy",
            "kill",
            "lick",
            "manga",
            "masturbation",
            "mobileWallpaper",
            "nsfwMobileWallpaper",
            "nsfwNeko",
            "nosebleed",
            "orgy",
            "public",
            "pantsu",
            "tentacles",
            "thighs",
            "uniform",
            "vagina",
            "yuri",
            "zettaiRyouiki",
        ],
        "api": "https://hmtai.hatsunia.cfd/v2/",
        "checker": "url",
    },
    "v4": {
        "end": [
            "doujin",
            "foxgirl",
            "gifs",
            "netorare",
            "maid",
            "panties",
            "school",
            "succubus",
            "uglybastard",
            "lewdneko",
        ],
        "api": "https://akaneko.cuteasfubuki.xyz/api/",
        "checker": "url",
    },
    "v5": {
        "end": ["nekolewd", "kitsune", "punch"],
        "api": "https://neko-love.xyz/api/v1/",
        "checker": "url",
    },
    "v6": {
        "end": ["furry", "ff", "futa", "nekoirl", "trap", "catboy"],
        "api": "https://api.xsky.dev/",
        "checker": "url",
    },
    "v7": {
        "end": ["jav", "rb"],
        "api": "https://scathach.redsplit.org/v3/nsfw/",
        "checker": "url",
    },
    "v8": {
        "end": ["fingering", "lesbian", "pussy", "fuck"],
        "api": "https://api.maher-zubair.tech/nsfw/",
        "checker": "url",
    },
}


def nekos(endpoint=None, endpoints=endpoints):
    if endpoint:
        for i in endpoints:
            if endpoint in endpoints[i]["end"]:
                api = endpoints[i]["api"]
                checker = endpoints[i]["checker"]
        result = requests.get(api + endpoint).json()
        return result[checker]
    return (
        endpoints["v1"]["end"]
        + endpoints["v2"]["end"]
        + endpoints["v3"]["end"]
        + endpoints["v4"]["end"]
        + endpoints["v5"]["end"]
        + endpoints["v7"]["end"]
        + endpoints["v8"]["end"]
    )


def nsfw(catagory):
    catagory.sort(key=str.casefold)
    horny = "**Catagory :** "
    for i in catagory:
        horny += f" `{i.lower()}` |"
    return horny


API = "https://catmemeapi2023.herokuapp.com/gimme"

""" 
async def importent(event):
    cat = ["-1001199597035", "-1001459701099", "-1001436155389", "-1001321431101"]
    if str(event.chat_id) in cat:
        await edit_or_reply(event, "**Yes I'm GAY**")
        await event.client.kick_participant(event.chat_id, "me")
        return True
    return False
"""

"""
hemtai = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "smug",
    "goose",
    "baka",
    "woof",
]
"""
