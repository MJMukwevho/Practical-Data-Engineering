from setuptools import setup, find_packages

setup(
    name="pylint_print_plugin",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "pylint.plugins": [
            "pylint_print_plugin = pylint_print_plugin:register",
        ],
    },
)
