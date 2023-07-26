# シンプルに比較できるように、バージョンをタプルで定義する
VERSION = (0, 0, 1)
# バージョン文字列をタプルから作成して、不整合を防ぐ
__version__ = ".".join([str(x) for x in VERSION])
