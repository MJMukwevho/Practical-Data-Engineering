from setuptools import setup, find_packages

setup(
    name="your_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pylint",
    ],
    entry_points={
        "pylint.plugins": [
            "print_checker = custom_checkers.custom_checkers",
        ],
    },
)
