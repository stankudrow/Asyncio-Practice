#!/usr/bin/env python3
"""Hello, asyncio."""


import asyncio
import time


# python3 00_hello_asyncio.py


def routine(sleep_time: int = 1) -> str:
    """Routine"""
    print(f"Coroutine is sleeping for {sleep_time} second[s].")
    time.sleep(sleep_time)
    return "hello, routine."


async def coroutine(sleep_time: int = 1) -> str:
    """Coroutine."""
    print(f"Coroutine is sleeping for {sleep_time} second[s].")
    await asyncio.sleep(sleep_time)
    return "Hello, coroutine."


async def main():
    """Entry point."""
    print(routine())
    print(await coroutine())


if __name__ == "__main__":
    asyncio.run(main())
