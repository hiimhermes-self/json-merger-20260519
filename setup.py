from setuptools import setup, find_packages

setup(
    name="json-merger",
    version="0.2.0",
    description="Recursive JSON merge utility. Nested dicts, list strategies, multiple files.",
    author="hiimhermes-self",
    url="https://github.com/hiimhermes-self/json-merger-20260519",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "json-merger=json_merger.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
