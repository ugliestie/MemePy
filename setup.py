import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="MemePy",
    version="1.2.4",
    description="Fork of meme generator for Python by Julian Brandt",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="ugliestie",
    author_email='ugliestie@proton.me',
    url="https://github.com/ugliestie/MemePy",
    packages=["MemePy"],
    package_data={"MemePy": ["Resources/*/*"]},
    license="MIT",
    install_requires=[
        "pillow",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
