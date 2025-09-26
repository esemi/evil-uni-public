"""
Напиши тесты на функции example_* ниже.
"""

import asyncio
import random
import time
from datetime import datetime, UTC
from typing import Any

import httpx

http_client = httpx.AsyncClient()


def example_1(*numbers) -> dict[str, Any]:
    if len(numbers) < 2:
        raise ValueError('Empty request')

    if any(num < 0 for num in numbers):
        raise ValueError('Positive numbers only')
    
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    
    return {
        'mean': mean,
        'sum': total,
        'count': count
    }


async def example_2(user_id: int, base_url: str = 'https://jsonplaceholder.typicode.com') -> dict[str, Any]:
    response = await http_client.get(f"{base_url}/users/{user_id}")
    response.raise_for_status()
    user_data = response.json()
    user_data['fetched_at'] = datetime.now(UTC).isoformat()
    return user_data


def example_3(draw_chance: int = 3, max_tries: int = 2) -> tuple[bool, int]:
    for try_number in range(max_tries):
        draw_result = random.randint(0, 100)
        if draw_result <= draw_chance:
            _deposit_to_winner()  # начисляем выигрыш пользователю
            return True, try_number
    return False, max_tries


def _deposit_to_winner() -> None:
    time.sleep(100)  # fake of huge database transaction


if __name__ == "__main__":
    print(example_1(1, 2, 5))
    print(asyncio.run(example_2(1)))
    print(example_3(30, 2))
