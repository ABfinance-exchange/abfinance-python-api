# ABfinance-ABfinance-python-api
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


Official Python3 API connector for ABFinance's HTTP and WebSockets APIs.

## Table of Contents

- [About](#about)
- [Development](#development)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)
- [Contributors](#contributors)
- [Donations](#donations)

## About
Put simply, `ABfinance-python-api`  is the official lightweight one-stop-shop module for the HTTP and WebSocket APIs. You're welcome to contribute!

It was designed with the following vision in mind:

> I was personally never a fan of auto-generated connectors that used a mosh-pit of various modules you didn't want (sorry, `bravado`) and wanted to build my own Python3-dedicated connector with very little external resources. The goal of the connector is to provide traders and developers with an easy-to-use high-performing module that has an active issue and discussion board leading to consistent improvements.

## Development
`ABfinance-python-api` is being actively developed, and new API changes should arrive on `ABfinance-python-api` very quickly. `ABfinance-python-api` uses `requests` and `websocket-client` for its methods, alongside other built-in modules. Anyone is welcome to branch/fork the repository and add their own upgrades. If you think you've made substantial improvements to the module, submit a pull request and we'll gladly take a look.

## Installation
`ABfinance-python-api` requires Python 3.9.1 or higher. The module can be installed manually or via [PyPI](https://pypi.org/project/ABfinance-python-api/) with `pip`:
```
pip install ABfinance-python-api
```

## Usage
You can retrieve a specific market like so:

```python
from abfinance_api.unified_trading import HTTP
```
Create an HTTP session and connect via WebSocket for Inverse on mainnet:
```python
session = HTTP(
    testnet=False,
    api_key="...",
    api_secret="...",
)
```
Information can be sent to, or retrieved from, the APIs:

```python
# Get the orderbook of the USDT Perpetual, BTCUSDT
session.get_orderbook(category="linear", symbol="BTCUSDT")

# Create five long USDC Options orders.
# (Currently, only USDC Options support sending orders in bulk.)
payload = {"category": "option"}
orders = [{
  "symbol": "BTC-30JUN23-20000-C",
  "side": "Buy",
  "orderType": "Limit",
  "qty": "0.1",
  "price": i,
} for i in [15000, 15500, 16000, 16500, 16600]]

payload["request"] = orders
# Submit the orders in bulk.
session.place_batch_order(payload)
```
Check out the example python files or the list of endpoints below for more information on available
endpoints and methods. 

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

