from abfinance_api.unified_trading import HTTP

session = HTTP(
    testnet=True,
    api_key="4Zr4UWR7X9v62rtrDu",
    api_secret="BCOvlHbm4oMGMrDkuDDkIpI0Bf0AwxQ4dzGy",
)

print(session.get_orderbook(category="linear", symbol="BTCUSDT"))
