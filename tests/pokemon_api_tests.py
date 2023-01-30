from src.pokemon_api import Pokeapi

pokemon_api = Pokeapi()
params = {
    "limit": 3000,
    "offset": 0
}


def test_pokeapi_status_code():
    res = pokemon_api.get_all_pokemons(params)
    assert res.status_code == 200


def test_response_is_not_empty():
    res = pokemon_api.get_all_pokemons(params).json()
    assert res["results"] != []


def test_response_has_all_pokemons():
    res = pokemon_api.get_all_pokemons(params).json()
    assert res["count"] == len(res["results"])


def test_response_time_under_1s():
    res = pokemon_api.get_all_pokemons(params)
    elapsed_time_in_ms = res.elapsed.microseconds // 1000
    assert elapsed_time_in_ms < 1000


def test_response_content_is_below_100kB():
    res = pokemon_api.get_all_pokemons(params)
    assert len(res.content) < 100000


def test_pokemon_pagination():
    params = {
        "limit": 10,
        "offset": 20
    }
    res = pokemon_api.get_all_pokemons(params).json()
    assert len(res["results"]) == params["limit"]
    assert str(params["offset"]+1) in res["results"][0]["url"]
    assert str(params["offset"]+params["limit"]) in res["results"][-1]["url"]
    id = 0
    for result in res["results"]:
        assert result["url"] == f"https://pokeapi.co/api/v2/pokemon/{params['offset']+1+id}/"
        id += 1
