from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="gcmi",
    version='0.3',
    description="Functions for calculating mutual information and other information theoretic quantities using a parametric Gaussian copula",
    author=["Robin Ince"],
    author_email="robin.ince@glasgow.ac.uk",
    pymodules=["gcmi"],
    install_requires=required,
)

