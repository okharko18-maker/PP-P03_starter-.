"""Відкриті приклади 13 (з картки). Повний набір перевірок — у викладача."""
import pytest
from conftest import load

M = load(13)
solve = M.solve

PUBLIC = [(('Кобзар|поезія; Енеїда|поезія; Тіні|проза', '2'),
  'Книг: 3\nУнікальних жанрів: 2\nПопулярні жанри (топ-2):\n1. поезія: 2\n2. проза: 1'),
 (('a|b|c; |x; y|; z', '3'), 'Помилка: немає даних')]


solve = M.solve


@pytest.mark.parametrize("args,expected", PUBLIC)
def test_public(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    for name in ('parse_items', 'build_index', 'rank', 'unique_sorted', 'solve'):
        assert callable(getattr(M, name, None)), f"немає функції {name}"
