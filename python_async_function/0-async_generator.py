#!/usr/bin/env python3
"""
Module 3-tasks

Provides a helper function that schedules the execution of the
wait_random coroutine as an asyncio.Task and returns the created Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum number of seconds to wait before
            the coroutine completes.

    Returns:
        asyncio.Task: A Task object wrapping wait_random(max_delay),
        scheduled on the current event loop.
    """
    return asyncio.create_task(wait_random(max_delay))
