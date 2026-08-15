"""
Тема: N+1 проблема (см. theory/software-engineering.md → «Выбор БД под задачу»).

Дано: «репозиторий» с двумя таблицами в памяти — авторы и их книги — и метод-заглушка
запроса к БД, который считает каждый вызов как отдельный запрос (self.queries).

Функция list_authors_with_books_naive делает 1 запрос на авторов + по запросу на
книги КАЖДОГО автора = N+1 запросов.

Задача: реализовать list_authors_with_books_batched так, чтобы получить тот же
результат за фиксированное число запросов (≈2, не зависящее от числа авторов) —
одним батч-запросом книг по списку author_id.

Проверка внизу: результат совпадает, а число запросов не растёт с числом авторов.
"""


class Repo:
    def __init__(self):
        self._authors = {1: 'Alex', 2: 'Mary', 3: 'John'}
        self._books = [
            {'id': 10, 'author_id': 1, 'title': 'A1'},
            {'id': 11, 'author_id': 1, 'title': 'A2'},
            {'id': 12, 'author_id': 2, 'title': 'M1'},
            {'id': 13, 'author_id': 3, 'title': 'J1'},
        ]
        self.queries = 0

    def all_authors(self) -> list[dict]:
        self.queries += 1
        return [{'id': aid, 'name': name} for aid, name in self._authors.items()]

    def books_of_author(self, author_id: int) -> list[dict]:
        self.queries += 1
        return [b for b in self._books if b['author_id'] == author_id]

    def books_of_authors(self, author_ids: list[int]) -> list[dict]:
        self.queries += 1
        return [b for b in self._books if b['author_id'] in author_ids]


def list_authors_with_books_naive(repo: Repo) -> list[dict]:
    authors = repo.all_authors()
    for author in authors:
        author['books'] = repo.books_of_author(author['id'])  # +1 запрос на каждого
    return authors


def list_authors_with_books_batched(repo: Repo) -> list[dict]:
    raise NotImplemented


def _result(rows: list[dict]) -> dict[int, list[str]]:
    return {a['id']: sorted(b['title'] for b in a['books']) for a in rows}


naive_repo = Repo()
naive = list_authors_with_books_naive(naive_repo)

batched_repo = Repo()
batched = list_authors_with_books_batched(batched_repo)

assert _result(naive) == _result(batched), 'результат должен совпадать с наивным'
assert naive_repo.queries == 4, 'наивный: 1 + N(=3)'
assert batched_repo.queries <= 2, f'батч должен быть ≈2 запроса, а не расти с N (было {batched_repo.queries})'
print('ok, queries:', naive_repo.queries, '->', batched_repo.queries)
