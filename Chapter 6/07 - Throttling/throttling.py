"""
"マルチスレッドを使用したアプリケーション例" のサンプルコード
マルチスレッド・アプリケーションにおけるスロットリング/レート制限の実装方法

"""
import time
from queue import Queue, Empty
from threading import Thread, Lock

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

THREAD_POOL_SIZE = 4


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = None

    def consume(self, amount=1):
        if amount > self.rate:
            raise ValueError("amountはrate以下でなければなりません")
        
        with self._consume_lock:
            now = time.time()

            # 経過時間の初期化を最初のリクエスト時刻で行い、
            # 初期の大量リクエスト送信を防止
            if self.last is None:
                self.last = now

            elapsed = now - self.last

            # 経過時間に応じてトークンを増やす
            if elapsed * self.rate > 1:
                self.tokens += elapsed * self.rate
                self.last = now

            # バケット溢れを防止
            self.tokens = min(self.rate, self.tokens)

            # トークンが利用可能なら消費して返す
            if self.tokens >= amount:
                self.tokens -= amount
                return amount

            return 0


def fetch_rates(base):
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}")

    response.raise_for_status()
    rates = response.json()["rates"]
    # note: 同じ通貨の交換レートは 1:1 となる。
    rates[base] = 1.0
    return base, rates


def present_result(base, rates):
    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def worker(work_queue, results_queue, throttle):
    while True:
        try:
            item = work_queue.get_nowait()
        except Empty:
            break

        while not throttle.consume():
            time.sleep(0.1)

        try:
            result = fetch_rates(item)
        except Exception as err:
            results_queue.put(err)
        else:
            results_queue.put(result)
        finally:
            work_queue.task_done()


def main():
    work_queue = Queue()
    results_queue = Queue()
    throttle = Throttle(10)

    for base in BASES:
        work_queue.put(base)

    threads = [
        Thread(target=worker, args=(work_queue, results_queue, throttle))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result, Exception):
            raise result

        present_result(*result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print(f"経過時間: {elapsed:.2f}s")
