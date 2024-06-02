from setuptools import setup

setup(
    name="print_and_show_checker",
    version="0.1",
    py_modules=["custom_checker"],
    entry_points={
        "pylint.checkers": [
            "print_and_show_checker = custom_checker:register",
        ],
    },
)
