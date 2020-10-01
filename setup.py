import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="np2ltx",
    version="0.1",
    author="Johannes Giercsky Nilssen",
    author_email="",
    description="Parse numpy to latex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonny-puma/np2ltx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
