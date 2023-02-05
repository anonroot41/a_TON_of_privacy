from setuptools import (
    setup,
    find_packages,
)

setup(
    name="atop",
    version="0.0.2-6",
    author="Aaarghhh",
    author_email="giacomo@udontneed.it",
    packages=["atop"],
    package_dir={'':'src'},
    include_package_data=True,
    entry_points={"console_scripts": ["a-ton-of-privacy = atop.atop:run"]},
    url="https://github.com/aaarghhh/a_TON_of_privacy",
    license="MIT",
    description='"A TON of Privacy" formally called ATOP ... is a tool for conducting OSINT investigations on TON NFTs.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "certifi == 2022.12.7",
        "charset-normalizer == 3.0.1",
        "colorama==0.4.6",
        "idna == 3.4",
        "pyaes == 1.6.1",
        "pyasn1 == 0.4.8",
        "requests ~= 2.28.2",
        "rsa == 4.9",
        "urllib3 == 1.26.14",
    ],
    zip_safe=False,
)
