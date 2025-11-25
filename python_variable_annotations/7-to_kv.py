#!/usr/bin/env python3
"""
This module contains a function that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the string k and the second is the square of v as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: Tuple of (k, square of v).
    """
    return (k, float(v ** 2))
