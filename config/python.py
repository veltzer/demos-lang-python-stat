config_requires = []
dev_requires = []
install_requires = [
    "numpy",
    "matplotlib",
    "scipy",
]
build_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
    "pycmdtools",
    "pydmt",
    "pylint",
    "flake8",
    "mypy",
]
test_requires = []
requires = config_requires + install_requires + build_requires + test_requires
