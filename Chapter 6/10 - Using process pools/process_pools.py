import time
from multiprocessing import Pool

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

POOL_SIZE = 4


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


def main():
    with Pool(POOL_SIZE) as pool:
        results = pool.map(fetch_rates, BASES)

    for result in results:
        present_result(*result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print(f"経過時間: {elapsed:.2f}s")