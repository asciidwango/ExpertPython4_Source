"""
"非同期プログラミング" のサンプルコード
非同期にprintするだけのコード

"""
import asyncio
import random

async def print_number(number):
    await asyncio.sleep(random.random())
    print(number)


async def main():
    await asyncio.gather(*[
        print_number(number)
        for number in range(10)
    ])


if __name__ == "__main__":
    asyncio.run(main())
