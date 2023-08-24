"""
"マルチプロセス" のサンプルコード
`multiprocessing`モジュールのパイプを通信チャネルとして使用する方法

"""
from multiprocessing import Process, Pipe


class CustomClass:
    pass


def worker(connection):
    while True:
        instance = connection.recv()
        if instance:
            print(f"子: 受信: {instance}")
        if instance is None:
            break


def main():
    parent_conn, child_conn = Pipe()

    child = Process(target=worker, args=(child_conn,))

    for item in (
        42,
        "some string",
        {"one": 1},
        CustomClass(),
        None,
    ):
        print("親: 送信: {}".format(item))
        parent_conn.send(item)

    child.start()
    child.join()


if __name__ == "__main__":
    main()
