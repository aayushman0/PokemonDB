from fastapi import FastAPI

from views import v1

app = FastAPI(
    title="Pokemons",
    description="List Pokemons",
)

app.include_router(v1.router, prefix="/v1")
