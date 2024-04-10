#!/usr/bin/env python
from setuptools import setup

setup(
    name="payout_calculator",
    install_requires=["currencyconverter"],
    packages=["payout_calculator"],
    entry_points={
        "console_scripts": [
            "payout-calc = payout_calculator.__main__:main",
        ]
    },
    extras_require={
        "dev": [
            "pre-commit>=3.6.2",
        ],
    },
)
