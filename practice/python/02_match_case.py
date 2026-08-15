"""
Тема: match/case, structural pattern matching (см. theory/python.md → «Что нового в Python»).

Реализуй describe_event(event) через match/case. На вход приходят разные по форме
события (dict-ы), надо вернуть человекочитаемую строку:

- {"type": "click", "x": .., "y": ..}          -> "click at (x, y)"
- {"type": "key", "key": ..}                    -> "key <key>"
- {"type": "scroll", "delta": ..} где delta > 0 -> "scroll up"
- {"type": "scroll", "delta": ..} где delta < 0 -> "scroll down"
- всё остальное                                 -> "unknown event"

Используй именно match/case со структурными паттернами (маппинги + guard),
а не цепочку if/elif по ключам.
"""


def describe_event(event: dict) -> str:
    raise NotImplemented


assert describe_event({"type": "click", "x": 10, "y": 20}) == "click at (10, 20)"
assert describe_event({"type": "key", "key": "Enter"}) == "key Enter"
assert describe_event({"type": "scroll", "delta": 3}) == "scroll up"
assert describe_event({"type": "scroll", "delta": -2}) == "scroll down"
assert describe_event({"type": "resize"}) == "unknown event"
print('ok')
