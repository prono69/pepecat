# By @kirito6969

import requests
from pokedex.pokedex import Pokedex

from ..core.managers import edit_delete, edit_or_reply
from . import catub

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
async def pokedex(event):
    pokemon = event.pattern_match.group(1).lower()
    if not pokemon:
        await edit_delete(event, "`Give a Pokemon Name`")
        return
    xx = await edit_or_reply(event, "`Booting up the pokedex.......`")
    move = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    rw = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
    w = requests.get(f"https://api.pokemontcg.io/v1/cards?name={pokemon}")
    lol = w.json()
    r = requests.get(rw)
    a = r.json()
    try:
        name = a["name"]
    except Exception:
        await edit_delete(event, "`Be sure To give correct Name`")
        return
    typ = a["type"]
    species = a["species"]
    abilities = a["abilities"]
    height = a["height"]
    weight = a["weight"]
    esatge = r.json()["family"]["evolutionStage"]
    try:
        weaknesses = lol["cards"][0]["weaknesses"][0]["type"]
    except BaseException:
        weaknesses = None
    l = r.json()["family"]["evolutionLine"]
    # ambiguous variable name 'l' flake8(E741)
    if not l:
        line = "None"
    else:
        line = ", ".join(map(str, l))
    gen = a["generation"]
    try:
        move1 = move.json()["moves"][0]["move"]["name"]
    except IndexError:
        move1 = None
    try:
        move2 = move.json()["moves"][1]["move"]["name"]
    except IndexError:
        move2 = None
    try:
        move3 = move.json()["moves"][2]["move"]["name"]
    except IndexError:
        move3 = None
    try:
        move4 = move.json()["moves"][3]["move"]["name"]
    except IndexError:
        move4 = None
    try:
        move5 = move.json()["moves"][4]["move"]["name"]
    except IndexError:
        move5 = None
    try:
        move6 = move.json()["moves"][5]["move"]["name"]
    except IndexError:
        move6 = None
    try:
        move7 = move.json()["moves"][6]["move"]["name"]
    except IndexError:
        move7 = None
    description = a["description"]
    typ = ", ".join(map(str, typ))
    Stats = a["stats"]
    species = ", ".join(map(str, species))
    abilities = ", ".join(map(str, abilities))
    poli = Pokedex()
    pname = poli.get_pokemon_by_name(pokemon)
    pokemon = pname[0]
    lst = pokemon.get("sprite")
    iname = f"{name}".upper()
    cap = f"""

**NAME** : `{iname}`
**TYPE** : `{typ}`
**SPECIES** : `{species}`
**Evolution Line** : `{line}`
**Evolution Stage** : `{esatge}`
**Generation** : `{gen}`

**ABILITIES** : `{abilities}`
**WEAKNESSES** :`{weaknesses}`
**HEIGHT** : `{height}`
**WEIGHT** : `{weight}`

    **Stats**                               **Moves**
**Hp**      : `{Stats['hp']}`               `(1){move1}`
**Attack**  : `{Stats['attack']}`           `(2){move2}`
**Defense** : `{Stats['defense']}`          `(3){move3}`
**Sp_atk**  : `{Stats['sp_atk']}`           `(4){move4}`
**Sp_def**  : `{Stats['sp_def']}`           `(5){move5}`
**Speed**   : `{Stats['speed']}`            `(6){move6}`
**Total**   : `{Stats['total']}`            `(7){move7}`

**DESCRIPTION** : `{description}`
  """
    await event.client.send_file(event.chat_id, lst, caption=cap)
    await xx.delete()


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
        await edit_delete(event, "`Be sure To give correct Name`", 5)
        return
