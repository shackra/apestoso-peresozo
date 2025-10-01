from setuptools import find_packages, setup

setup(
    name="apestoso-peresozo",
    version="0.1.1",
    description="graba entradas de controles y los reproduce en GNU/Linux",
    author="Jorge Javier Araya Navarro",
    author_email="jorge@esavara.cr",
    license="GPL-3.0-or-later",
    packages=find_packages(),
    install_requires=[
        "evdev>=1.6.1",
    ],
    entry_points={
        "console_scripts": [
            "apestoso=grabar:__main__",
            "peresozo=reproducir:__main__",
        ],
    },
    python_requires=">=3.11",
)
