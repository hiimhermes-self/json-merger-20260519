from setuptools import setup, find_packages

setup(
    name="json-merger",
    version="0.1.0",
    description="Recursive JSON merge utility. Merges multiple JSON files with nested override support.",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "json-merger=json_merger.__main__:main",
        ],
    },
)
