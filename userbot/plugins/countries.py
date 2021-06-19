# Kanged from FridayUserBot
# Ported by @kirito6969

import flag
from countryinfo import CountryInfo

from ..core.managers import edit_delete, edit_or_reply
from . import catub

plugin_category = "extra"


@catub.cat_cmd(
    pattern="country ?(.*)",
    command=("country", plugin_category),
    info={
        "header": "Get Information About any Country",
        "usage": "{tr}country <country name>",
        "example": "{tr}country India",
    },
)
async def country_(message):
    await edit_or_reply(message, "`Searching For Country.....`")
    lol = message.pattern_match.group(1)
    if not lol:
        await edit_delete(message, "`Please Give Input!`")
        return
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await edit_delete(
            message, "`Country Not Found. Maybe You Need to Learn Geography!`"
        )
        return
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = ""
    for p in bb:
        hu += p + ",  "
    area = a.get("area")
    borders = ""
    hell = a.get("borders")
    for fk in hell:
        borders += fk + ",  "
    call = ""
    WhAt = a.get("callingCodes")
    for what in WhAt:
        call += what + "  "
    capital = a.get("capital")
    currencies = ""
    fker = a.get("currencies")
    for FKer in fker:
        currencies += FKer + ",  "
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += po + ",  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)
    languages = a.get("languages")
    lMAO = ""
    for lmao in languages:
        lMAO += lmao + ",  "
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = ""
    for jerry in tik:
        tom += jerry + ",   "
    GOT = a.get("tld")
    lanester = ""
    for targaryen in GOT:
        lanester += targaryen + ",   "
    wiki = a.get("wiki")
    caption = f"""<b><u>information gathered successfully</b></u>
<b>
Country Name:- {name}  {okie}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
population:- {waste}
Region:- {reg}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}

Wikipedia:-</b> <code>{wiki}</code>

<u><b>Information Gathered By PepeCat.</b></u>
"""
    await edit_or_reply(message, caption, parse_mode="html")
