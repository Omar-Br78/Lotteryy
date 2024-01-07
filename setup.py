import setuptools
from lottery_DCL import*

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lottery_DCL',
    version='0.1.1',
    author="Omar Bourkab",
    author_email="omarr.bourkab@gmail.com",
    description="Lottery utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(where="."),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
