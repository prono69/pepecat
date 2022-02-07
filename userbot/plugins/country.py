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
    hu = "".join(f"{p},  " for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(f"{fk},  " for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(f"{what}  " for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(f"{FKer},  " for FKer in fker)
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
        iso += f"{po},  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)
    languages = a.get("languages")
    lMAO = "".join(f"{lmao},  " for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(f"{jerry},   " for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(f"{targaryen},   " for targaryen in GOT)
    wiki = a.get("wiki")
    caption = f"""<b>✨ Information of {name}</b>
<b>
Country Name:- {name}  {okie}
Native Name:- {nonive}
Alternative Spellings:- {hu}
Population:- {waste}
Capital:- {capital}
Languages:- {lMAO}
Region:- {reg}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's currency:- {currencies}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}

Wikipedia:-</b> <code>{wiki}</code>

<b>✨ Information Gathered By PepeCat.</b>
"""
    await edit_or_reply(message, caption, parse_mode="html", link_preview=False)
