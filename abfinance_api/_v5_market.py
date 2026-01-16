from ._http_manager import _V5HTTPManager
from .market import Market


class MarketHTTP(_V5HTTPManager):
    def get_server_time(self) -> dict:
        """
        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_SERVER_TIME}",
        )

    def get_kline(self, **kwargs) -> dict:
        """Query the kline data. Charts are returned in groups based on the requested interval.

        Required args:
            category (string): Product type: spot,linear,inverse
            symbol (string): Symbol name
            interval (string): Kline interval.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_KLINE}",
            query=kwargs,
        )

    def get_instruments_info(self, **kwargs):
        """Query a list of instruments of online trading pair.

        Required args:
            category (string): Product type. spot,linear,inverse,option

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_INSTRUMENTS_INFO}",
            query=kwargs,
        )

    def get_orderbook(self, **kwargs):
        """Query orderbook data

        Required args:
            category (string): Product type. spot, linear, inverse, option
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_ORDERBOOK}",
            query=kwargs,
        )

    def get_tickers(self, **kwargs):
        """Query the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.

        Required args:
            category (string): Product type. spot,linear,inverse,option

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_TICKERS}",
            query=kwargs,
        )

    def get_public_trade_history(self, **kwargs):
        """Query recent public trading data.

        Required args:
            category (string): Product type. spot,linear,inverse,option
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_PUBLIC_TRADING_HISTORY}",
            query=kwargs,
        )

    def get_price_limit(self, **kwargs):
        """
        Required args:
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_PRICE_LIMIT}",
            query=kwargs,
        )

    def get_rpi_orderbook(self, **kwargs):
        """Query RPI orderbook data.

        Required args:
            category (string): Product type. spot, linear, inverse
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_RPI_ORDERBOOK}",
            query=kwargs,
        )

    def get_index_price_components(self, **kwargs):
        """Get index price components.

        Required args:
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_INDEX_PRICE_COMPONENTS}",
            query=kwargs,
        )
