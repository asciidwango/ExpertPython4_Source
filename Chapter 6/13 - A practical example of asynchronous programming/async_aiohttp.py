"""
"非同期プログラミング" のサンプルコード
aiohttpを使用して非同期HTTPコールを実行する方法を示す例

"""
import asyncio
import time

import aiohttp

from asyncrates import get_rates

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


def present_result(base, rates):
    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


async def main():
    async with aiohttp.ClientSession() as session:
        for result in await asyncio.gather(*[
            get_rates(session, base) for base in BASES]
        ):
            present_result(*result)


if __name__ == "__main__":
    started = time.time()
    asyncio.run(main())
    elapsed = time.time() - started

    print()
    print(f"経過時間: {elapsed:.2f}s")
