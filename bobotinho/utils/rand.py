# -*- coding: utf-8 -*-
import random
from typing import Union


def random_line_from_txt(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        random_line = random.choice(f.read().splitlines())
    return random_line


def random_number(*, min: int = 0, max: int = 100, div: int = 1) -> float:
    if div != 1:
        return random.randint(min, max) / div
    return random.randint(min, max)


def random_choice(options: Union[str, list[str]], *, sep: str = None) -> str:
    if isinstance(options, str):
        options = options.split(sep)
    return random.choice(options)


def random_choices(options: Union[str, list[str]], *, sep: str = None, k: int = 1) -> list[str]:
    if isinstance(options, str):
        options = options.split(sep)
    return random.choices(options, k=k)