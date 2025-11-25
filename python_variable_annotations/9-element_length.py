#!/usr/bin/env python3
"""
This module contains a function that returns a list of tuples of iterable elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from lst and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples with (element, length).
    """
    return [(i, len(i)) for i in lst]
