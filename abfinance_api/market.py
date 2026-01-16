from enum import Enum


class Market(str, Enum):
    GET_SERVER_TIME = "/v5/market/time"
    GET_KLINE = "/v5/market/kline"
    GET_INSTRUMENTS_INFO = "/v5/market/instruments-info"
    GET_ORDERBOOK = "/v5/market/orderbook"
    GET_TICKERS = "/v5/market/tickers"
    GET_PUBLIC_TRADING_HISTORY = "/v5/market/recent-trade"
    GET_PRICE_LIMIT = "/v5/market/price-limit"
    GET_RPI_ORDERBOOK = "/v5/market/rpi_orderbook"
    GET_INDEX_PRICE_COMPONENTS = "/v5/market/index-price-components"

    def __str__(self) -> str:
        return self.value
