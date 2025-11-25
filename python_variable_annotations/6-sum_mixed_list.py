#!/usr/bin/env python3
"""
This module contains a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all numbers in a list of ints and floats and return the total as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and/or floats.

    Returns:
        float: The sum of the list elements as float.
    """
    return float(sum(mxd_lst))
