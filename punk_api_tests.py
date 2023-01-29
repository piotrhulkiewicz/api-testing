import requests
import datetime


def test_default_beers():
    response = requests.get("https://api.punkapi.com/v2/beers")
    status_code = response.status_code
    body = response.json()
    assert status_code == 200
    assert body[0]["id"] == 1
    assert body[-1]["id"] == 25
    assert len(body) == 25


def test_response_has_beers_with_id_11_to_20():
    params = {
        "ids": "11|12|13|14|15|16|17|18|19|20"
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert response.status_code == 200
    assert len(body) == 10

    beer_id = 11
    for beer in body:
        assert beer["id"] == beer_id
        beer_id += 1


def test_beer_with_id_123():
    params = {
        "ids": 123
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert response.status_code == 200
    assert body[0]["id"] == 123


def test_response_has_20_beers_from_page_5():
    params = {
        "page": 5,
        "per_page": 20
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert response.status_code == 200
    assert body[0]["id"] == 81
    assert len(body) == 20


def test_beer_with_abv_in_range_from_5_to_7():
    params = {
        "abv_gt": 4.9,
        "abv_lt": 7.1
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert response.status_code == 200
    for beer in body:
        assert 4.9 < beer["abv"] < 7.1


def test_beer_brewed_in_2010():
    params = {
        "brewed_after": "12-2009",
        "brewed_before": "01-2011"
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert response.status_code == 200
    for beer in body:
        assert "2010" in beer["first_brewed"]
