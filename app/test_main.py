import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (29, [4, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4])
    ],
    ids=[
        "one penny",
        "six cents",
        "seventeen cents",
        "fifty cents",
        "zero cents",
        "four cents",
        "five cents",
        "ten cents",
        "twenty-five cents",
        "twenty-nine cents",
        "ninety-nine cents",
        "one hundred cents"
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected, (
        f"Expected {expected} for {cents} cents"
    )
