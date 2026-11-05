"""Практична робота PP-P03. Варіант 13: Жанри бібліотеки.

Реалізуйте п'ять функцій за карткою варіанта. Введення й виведення — лише в блоці __main__.
"""


def parse_items(text: str) -> list:
    """Розбирає вхідний рядок і нормалізує елементи за правилами картки."""
    items = []

    for record in text.split(";"):
        if record.count("|") != 1:
            continue

        title, genre = record.split("|")

        if title.strip() and genre.strip():
            items.append(genre.strip().lower())

    return items


def build_index(items: list) -> dict:
    """Будує словник-індекс за правилом картки."""
    index = {}

    for genre in items:
        index[genre] = index.get(genre, 0) + 1

    return index


def rank(index: dict, n: int) -> list:
    """Повертає n найкращих пар (ключ, значення) як список кортежів."""
    if n <= 0:
        return []

    return sorted(
        index.items(),
        key=lambda item: (-item[1], item[0])
    )[:n]


def unique_sorted(items: list) -> list:
    """Повертає унікальні елементи, відсортовані за правилом картки."""
    return sorted(set(items), key=lambda genre: (len(genre), genre))


def solve(text: str, n: str) -> str:
    """Збирає звіт за шаблоном картки."""
    n = n.strip()

    if not n or not n.isdigit():
        return "Помилка: n має бути цілим невід'ємним числом"

    n = int(n)
    items = parse_items(text)

    if not items:
        return "Помилка: немає даних"

    index = build_index(items)
    unique = unique_sorted(items)
    rating = rank(index, n)

    result = [
        f"Книг: {len(items)}",
        f"Унікальних жанрів: {len(unique)}",
        f"Популярні жанри (топ-{n}):"
    ]

    for i, (genre, count) in enumerate(rating, start=1):
        result.append(f"{i}. {genre}: {count}")

    return "\n".join(result)


if __name__ == "__main__":
    print(solve(input("Введіть текст: "), input("Введіть n: ")))

