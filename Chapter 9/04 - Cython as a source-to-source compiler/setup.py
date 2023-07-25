import os

from setuptools import setup, Extension

try:
    # 特定の環境変数が設定されていて、なおかつCythonがimportできる場合にだけ、
    # トランスパイルを行います。
    USE_CYTHON = bool(os.environ.get("USE_CYTHON"))
    import Cython
except ImportError:
    USE_CYTHON = False

ext = ".py" if USE_CYTHON else ".c"

extensions = [Extension("fibonacci", ["fibonacci" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name="fibonacci",
    ext_modules=extensions,
    extras_require={
        # '[with-cython]'をパッケージのインストール時に指定することで、
        # 指定したバージョンのCythonがインストールされます。
        "with-cython": ["cython==0.29.34"]
    },
)
