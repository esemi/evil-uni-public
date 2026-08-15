# Практика

Задачи-заготовки — в них специально оставлены дыры (`raise NotImplemented`, пустые
классы, `# todo`), твоя цель — их закрыть. Закрепляешь руками то, что прогнал по
теории в [`../theory/`](../theory/). Разбито по блокам зеркально теории.

## Блоки

| Блок | О чём | Теория |
|------|-------|--------|
| [Python](python/README.md) | Язык и внутренности: по одной задаче на каждую тему теории — новинки (dataclasses, match/case, typing), мутабельность, замыкания, `__hash__`/`__slots__`, контекст-менеджеры, `__new__`, mixins/MRO, GIL, asyncio, тесты, JWT, stateless, сигналы. | [`python.md`](../theory/python.md) |
| [Программная инженерия](software-engineering/README.md) | Backend-инженерия: индексы, N+1, дедлоки, очереди/ACK, HTTP retry + error budget, плюс инфра-практика — FastAPI в docker/minikube, линтеры (ruff/vulture/mypy), CI на GitHub Actions. | [`software-engineering.md`](../theory/software-engineering.md) |

Каждый блок — со своим README: список задач + пометка, каких тем из теории пока нет.
