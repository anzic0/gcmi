from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

exec(open("gcmi.py").read())
setup(
    name="gcmi",
    version=__version__,
    description="Functions for calculating mutual information and other information theoretic quantities using a parametric Gaussian copula",
    author=["Robin Ince"],
    author_email="robin.ince@glasgow.ac.uk",
    install_requires=required,
    pymodules=["gcmi"],
)

