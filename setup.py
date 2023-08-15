from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="sonne",
    version="0.0.1",
    description="Sonne is a Python module that provides a lot of possibilities to make your terminal look beautiful.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/sonnelib/sonne",
    author="Ekin Aksu",
    author_email="sonnelib@gmail.com",
    license="Apache License 2.0",
    keywords="Terminal, Style, Color, Terminal Styling",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    python_requires=">=3.8",
)
