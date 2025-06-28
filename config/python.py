""" python deps for this project """

install_requires: list[str] = [
    "numpy",
    "matplotlib",
    "scipy",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    "pycmdtools",
    "ruff",
    "pylint",
    "mypy",
]
requires = install_requires + build_requires
