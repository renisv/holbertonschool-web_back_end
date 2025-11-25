#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies its input by multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
