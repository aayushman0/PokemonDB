import requests
from dotenv import dotenv_values
from fastapi import APIRouter, HTTPException

from models import session, Pokemon

env: dict[str, str] = dotenv_values(".env")

router = APIRouter()


@router.get("/update-pokedb/")
def update_pokedb() -> dict[str, str]:
    response = requests.get(url=env.get("POKEAPI_URL"))

    if response.status_code != 200:
        raise HTTPException(
            status_code=400,
            detail=f"PokeAPI returned status code {response.status_code}")

    pokemons: list[dict[str, str] | None] = response.json().get("results", [])
    new_data_count = 0
    for pokemon in pokemons:
        name: str | None = pokemon.get("name", None)
        url: str | None = pokemon.get("url", None)
        if None in (name, url):
            continue

        pokemon_model: Pokemon | None = session.query(Pokemon).filter(Pokemon.name == name).scalar()
        if pokemon_model is not None:
            continue

        pokemon_detail_response = requests.get(url=url)
        pokemon_detail: dict = pokemon_detail_response.json()
        type_str: str = ""
        for type in pokemon_detail.get("types", []):
            type_str = type_str + type.get("type", {}).get("name", None) + " "
        image: str = pokemon_detail.get("sprites", {}).get("front_default", None)

        pokemon_model = Pokemon(name=name, type=type_str, image=image)
        session.add(pokemon_model)
        new_data_count += 1

    session.commit()
    return {"message": f"{new_data_count} new Pokemon/s added to the database."}


@router.get("/pokemons/")
def get_filtered_pokemons(name: str | None = None, type: str | None = None) -> list[dict[str, int | str] | None]:
    pokemons = session.query(Pokemon)
    if name:
        pokemons = pokemons.filter(Pokemon.name.contains(name))
    if type:
        pokemons = pokemons.filter(Pokemon.type.contains(type))
    result = [
        {
            "id": pokemon.id,
            "name": pokemon.name,
            "type": pokemon.type,
            "image": pokemon.image,
        } for pokemon in pokemons]

    return result
