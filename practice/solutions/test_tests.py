import asyncio
import os
import sys

import httpx
import respx
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from practice.pytest import example_1, example_2, example_3



# =============== example_1

def test_example_1_success():
    numbers = 1, 2, 3

    rslt = example_1(*numbers)

    assert rslt
    assert rslt['mean']
    assert rslt['sum']
    assert rslt['count']

    ttl = sum(numbers)
    cnt = len(numbers)

    assert rslt['mean'] == ttl/cnt
    assert rslt['sum'] == ttl
    assert rslt['count'] == cnt


def test_example_1_empty_request():

    nmbr = 1,

    with pytest.raises(ValueError) as exc:
        rslt = example_1()

    assert 'empty request' in str(exc.value).lower()


    with pytest.raises(ValueError) as exc:
        rslt = example_1(*nmbr)
    assert 'empty request' in str(exc.value).lower()


def test_example_1_negative_number():
    nmbrs = -3, 4, 6, 7

    with pytest.raises(ValueError) as exc:
        rslt = example_1(*nmbrs)

    assert 'positive numbers only' in str(exc.value).lower()


# =============== example_2 

@pytest.mark.asyncio
async def test_example_2_mocked():
    _user_id = 1
    fake_data = {
        'id': _user_id,
        'name': 'Leanne Graham',
        'username': 'Bret',
        'email': 'Sincere@april.biz',
        'address':
            {
                'street': 'Kulas Light',
                'suite': 'Apt. 556',
                'city': 'Gwenborough',
                'zipcode': '92998-3874',
                'geo': {'lat': '-37.3159', 'lng': '81.1496'}
            },
        'phone': '1-770-736-8031 x56442',
        'website': 'hildegard.org',
        'company':
            {
                'name': 'Romaguera-Crona',
                'catchPhrase': 'Multi-layered client-server neural-net',
                'bs': 'harness real-time e-markets'
            },
        'fetched_at': '2025-09-28T09:10:55.375622+00:00'
    }

    async with respx.mock:
        respx.get(f'https://jsonplaceholder.typicode.com/users/{_user_id}').mock(
            return_value=httpx.Response(200, json=fake_data)
        )

        rslt = await example_2(_user_id)

        assert rslt['id'] == _user_id
        assert rslt['address']
        assert rslt['username']


@pytest.mark.asyncio
async def test_example_2_not_found():
    _user_id = 0

    async with respx.mock:
        respx.get(f'https://jsonplaceholder.typicode.com/users/{_user_id}').mock(
            return_value=httpx.Response(404)
        )

        with pytest.raises(httpx.HTTPStatusError) as exc:
            rslt = await example_2(_user_id)

        assert exc.value.response.status_code == 404


# =============== example_3

def test_example_3_success(monkeypatch):

    _draw_chance = 3
    _max_tries = 2
    monkeypatch.setattr("practice.pytest._deposit_to_winner", lambda: None)

    monkeypatch.setattr("random.randint", lambda a, b: 1)

    won, try_number = example_3(draw_chance=_draw_chance, max_tries=_max_tries)


    assert won
    assert try_number == 0

def test_example_3_loser(monkeypatch):
    _draw_chance = 3
    _max_tries = 2

    monkeypatch.setattr("practice.pytest._deposit_to_winner", lambda: None)

    monkeypatch.setattr("random.randint", lambda a, b: 50)

    won, try_number = example_3(draw_chance=_draw_chance, max_tries=_max_tries)

    assert not won
    assert try_number == 2