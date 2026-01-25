from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='abfinance-python-api',
    version='1.0.3',
    description='Python3 HTTP/WebSocket API Connector',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ABfinance-exchange/abfinance-python-api",
    license="MIT License",
    author="Johnny",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="api connector",
    packages=["abfinance_api"],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "websocket-client",
        "pycryptodome",
    ],
)
