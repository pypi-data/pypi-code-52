from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="parts",
    version="0.1.0.0",
    packages=["parts",],
    install_requires=[],
    license="MIT",
    url="https://github.com/lapets/parts",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Minimal Python library for common list functions "+\
                "related to partitioning lists.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
