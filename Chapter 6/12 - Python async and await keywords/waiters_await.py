"""
"非同期プログラミング" のサンプルコード
2つのコルーチンがブロッキング呼び出し時にイベントループに制御を解放することで協調する例

"""
import asyncio
import random


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(f"{name} waited {time_to_sleep} seconds")


async def main():
    await asyncio.gather(waiter("first"), waiter("second"))


if __name__ == "__main__":
    asyncio.run(main())

