from setuptools import setup

setup(
    name="MathLibPy",
    version="0.0.0",
    url="http://github.com/jackromo/mathLibPy",
    license="MIT",
    description="Math library for Python",
    author="Jack Romo",
    author_email="sharrackor@gmail.com",
    platforms="any",
    packages=['mathlibpy'],
    install_requires=[
        "sphinx>=1.3.6"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python 2.7"
    ]
)
