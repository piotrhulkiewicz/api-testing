import requests


class Pokeapi:

    base_url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"

    def get_all_pokemons(self, params=None):

        response = requests.get(self.base_url + self.pokemon_endpoint, params=params)
        assert response.status_code == 200
        return response
