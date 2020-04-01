#!/usr/bin/env python3

import setuptools
from cloudinary_cli import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudinary-cli",
    version=__version__,
    author="Cloudinary, Brian Luk",
    author_email="info@cloudinary.com, lukitsbrian@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="A command line interface for Cloudinary with full API support",
    entry_points={
        'console_scripts': [
            'cld=cloudinary_cli.cli:main',
            'cloudinary=cloudinary_cli.cli:main',
            ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudinary/cloudinary-cli",
    packages=setuptools.find_packages(),
    keywords='cloudinary cli pycloudinary image video digital asset management command line interface transformation '
             'friendly easy flexible',
    license="MIT",
    python_requires='>=3.6.0',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=[
        "cloudinary",
        "pygments",
        "jinja2",
        "click",
        "click-log",
        "requests"
    ],
    include_package_data=True,
    zip_safe=False
)
