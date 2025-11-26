#!/usr/bin/env python3
"""
Async generator coroutine that yields 10 random numbers asynchronously with a delay.
"""

import asyncio
import random

async def async_generator():
    """
    Asynchronously generates 10 random numbers between 0 and 10 (float).
    Each number is yielded after an asynchronous 1 second delay.

    Yields:
        float: A random floating point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
