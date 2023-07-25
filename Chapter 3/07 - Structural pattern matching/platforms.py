import sys

match sys.platform:
    case "windows":
        print("Windowsでの実行")
    case "darwin" :
        print("macOSでの実行")
    case "linux":
        print("Linuxでの実行")
    case _:
        raise NotImplementedError(
            f"{sys.platform} は、サポートされていません!"
        )
