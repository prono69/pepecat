# By @kirito6969

import requests
from . import catub
from ..core.managers import edit_or_reply, edit_delete

plugin_category = "fun"

@catub.cat_cmd(
    pattern="pokemon ?(.*)",
    command=("pokemon", plugin_category),
    info={
        "header": "Get information about a Pokemon",
        "usage": "{tr}pokemon <pokemon name>",
        "examples": "{tr}pokemon Suicune",
    },
)
async def pokedex(message):
    pablo = await edit_or_reply(message, "`Searching For Pokémon.....`")
    sgname = message.pattern_match.group(1)
    if not sgname:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    url = f"https://starkapis.herokuapp.com/pokedex/{sgname}"
    r = requests.get(url).json()
    pokemon = r
    if pokemon.get("error") is not None:
        kk = f"""
Error:   {pokemon.get("error")}"""
        await pablo.edit(kk)
        return
    name = str(pokemon.get("name"))
    number = str(pokemon.get("number"))
    species = str(pokemon.get("species"))
    typo = pokemon.get("types")
    types = ""
    for tu in typo:
        types += str(tu) + ",  "

    lol = pokemon.get("abilities")
    lmao = lol.get("normal")
    ok = ""
    for ty in lmao:
        ok = str(ty) + ",  "

    kk = lol.get("hidden")
    hm = ""
    for pq in kk:
        hm += str(pq) + ",  "
    hell = pokemon.get("eggGroups")
    uio = ""
    for x in hell:
        uio += str(x) + ",  "

    height = pokemon.get("height")
    weight = pokemon.get("weight")
    yes = pokemon.get("family")
    Id = str(yes.get("id"))
    evo = str(yes.get("evolutionStage"))
    pol = yes.get("evolutionLine")
    xy = ""
    for p in pol:
        xy += str(p) + ",  "

    start = pokemon.get("starter")
    if not start:
        start = "No"
    elif start:
        start = "True"
    else:
        pass

    leg = pokemon.get("legendary")

    if not leg:
        leg = "No"
    elif leg:
        leg = "True"
    else:
        pass

    myt = pokemon.get("mythical")
    if not myt:
        myt = "No"
    elif myt:
        myt = "True"
    else:
        pass
    ultra = pokemon.get("ultraBeast")

    if not ultra:
        ultra = "No"
    elif ultra:
        ultra = "True"
    else:
        pass

    megA = pokemon.get("mega")

    if not megA:
        megA = "No"
    elif megA:
        megA = "True"
    else:
        pass

    gEn = pokemon.get("gen")
    link = pokemon.get("sprite")
    des = pokemon.get("description")
    caption = f"<b><u>Pokemon Information Gathered Successfully</b></u>\n\n\n<b>Name:-   {name}\nNumber:-  {number}\nSpecies:- {species}\nType:- {types}\n\n<u>Abilities</u>\nNormal Abilities:- {ok}\nHidden Abilities:- {hm}\nEgg Group:-  {uio}\nHeight:- {height}\nWeight:- {weight}\n\n<u>Family</u>\nID:- {Id}\nEvolution Stage:- {evo}\nEvolution Line:- {xy}\nStarter:- {start}\nLegendary:- {leg}\nMythical:- {myt}\nUltra Beast:- {ultra}\nMega:- {megA}\nGen:-  {gEn}\n\nDescription:-  <i>{des}</i></b>"

    await message.client.send_file(
        message.chat_id,
        file=link,
        caption=caption,
        parse_mode="HTML",
    )
    await pablo.delete()


@catub.cat_cmd(
    pattern="pokecard ?(.*)",
    command=("pokecard", plugin_category),
    info={
        "header": "Get information about a Pokemon Card",
        "usage": "{tr}pokecard <pokemon name>",
        "examples": "{tr}pokecard Rayquaza",
    },
)
async def pokecard(event):
    pokename = event.pattern_match.group(1)
    if not pokename:
        await edit_or_reply(event, "`Give A Pokemon name`")
        return
    rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
    r = requests.get(rw)
    a = r.json()
    try:
        o = a["cards"][0]["imageUrlHiRes"]
        await event.client.send_file(
            await event.client.get_input_entity(event.chat_id), o
        )
        await event.delete()
    except BaseException:
        await edit_delete(event, "`Be sure To give correct Name`",5)
        return
