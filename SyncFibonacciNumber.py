import asyncio
import random


async def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return await fib(n - 1) + await fib(n - 2)

async def fib_with_delay(n):
    await asyncio.sleep(random.random())  # Adding random delay up to 1 second
    return await fib(n)