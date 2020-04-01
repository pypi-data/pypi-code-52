import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serial-tool",  # Replace with your own username
    version="0.0.1",
    author="zcq100",
    author_email="zcq100@gmail.com",
    description="A serial tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zcq100/serial-tool",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "serial-tool=serial_tool.serial:main"
        ]
    },
    install_requires=[
        "pyserial"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
