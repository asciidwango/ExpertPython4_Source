"""
"マルチプロセス" のサンプルコード
POSIXシステム上でos.forkを使って新しいプロセスを生成する方法

"""
import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("子: こんにちは、私は子プロセスです")
        print(f"子: 私が知っているPID番号は {pid_list} です")

    else:
        pid_list.append(os.getpid())
        print()
        print("親: こんにちは、私は親プロセスです")
        print(f"親: 子プロセスのPID番号は  {child_pid} です")
        print(f"親: 私が知っているPID番号は {pid_list} です")


if __name__ == "__main__":
    main()
