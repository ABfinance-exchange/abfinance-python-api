import logging
from dataclasses import dataclass
from typing import Union
from abfinance_api.exceptions import (
    InvalidChannelTypeError,
    TopicMismatchError,
    UnauthorizedExceptionError,
)
from ._v5_market import MarketHTTP
from ._v5_trade import TradeHTTP
from ._v5_account import AccountHTTP
from ._v5_asset import AssetHTTP
from ._v5_earn import EarnHTTP
from ._v5_apilimit import ApiLimitHTTP
from ._websocket_stream import _V5WebSocketManager
from ._websocket_trading import _V5TradeWebSocketManager


logger = logging.getLogger(__name__)

WSS_NAME = "Unified V5"
PRIVATE_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.{TLD}/v5/private"
PUBLIC_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.{TLD}/v5/public/{CHANNEL_TYPE}"
AVAILABLE_CHANNEL_TYPES = [
    "spot",
    "private",
]


@dataclass
class HTTP(
    MarketHTTP,
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    EarnHTTP,
    ApiLimitHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)


class WebSocket(_V5WebSocketManager):
    def _validate_public_topic(self):
        if "/v5/public" not in self.WS_URL:
            raise TopicMismatchError(
                "Requested topic does not match channel_type"
            )

    def _validate_private_topic(self):
        if not self.WS_URL.endswith("/private"):
            raise TopicMismatchError(
                "Requested topic does not match channel_type"
            )

    def __init__(
        self,
        channel_type: str,
        **kwargs,
    ):
        super().__init__(WSS_NAME, **kwargs)
        if channel_type not in AVAILABLE_CHANNEL_TYPES:
            raise InvalidChannelTypeError(
                f"Channel type is not correct. Available: {AVAILABLE_CHANNEL_TYPES}"
            )

        if channel_type == "private":
            self.WS_URL = PRIVATE_WSS
        else:
            self.WS_URL = PUBLIC_WSS.replace("{CHANNEL_TYPE}", channel_type)
            # Do not pass keys and attempt authentication on a public connection
            self.api_key = None
            self.api_secret = None

        if (
            self.api_key is None or self.api_secret is None
        ) and channel_type == "private":
            raise UnauthorizedExceptionError(
                "API_KEY or API_SECRET is not set. They both are needed in order to access private topics"
            )

        self._connect(self.WS_URL)

    # Private topics

    def order_stream(self, callback):
        """Subscribe to the order stream to see changes to your orders in real-time.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "order"
        self.subscribe(topic, callback)

    def execution_stream(self, callback):
        """Subscribe to the execution stream to see your executions in real-time.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "execution"
        self.subscribe(topic, callback)

    def wallet_stream(self, callback):
        """Subscribe to the wallet stream to see changes to your wallet in real-time.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "wallet"
        self.subscribe(topic, callback)

    # Public topics

    def orderbook_stream(self, depth: int, symbol: Union[str, list], callback):
        """Subscribe to the orderbook stream. Supports different depths.

        Spot:
        Level 1 data, push frequency: 10ms
        Level 50 data, push frequency: 20ms

        Required args:
            symbol (string/list): Symbol name(s)
            depth (int): Orderbook depth

        """
        self._validate_public_topic()
        topic = f"orderbook.{depth}." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def rpi_orderbook_stream(self, symbol: Union[str, list], callback):
        """Subscribe to the RPI orderbook stream.

        Spot:
        Level 50 data, push frequency: 100ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = f"orderbook.rpi." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def trade_stream(self, symbol: Union[str, list], callback):
        """Subscribe to the recent trades stream.
        After subscription, you will be pushed trade messages in real-time.

        Push frequency: real-time

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = f"publicTrade." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def ticker_stream(self, symbol: Union[str, list], callback):
        """Subscribe to the ticker stream.

        Push frequency: 100ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = "tickers.{symbol}"
        self.subscribe(topic, callback, symbol)

    def kline_stream(self, interval: int, symbol: Union[str, list], callback):
        """Subscribe to the klines stream.

        Push frequency: 1-60s

        Required args:
            symbol (string/list): Symbol name(s)
            interval (int): Kline interval

        """
        self._validate_public_topic()
        topic = f"kline.{interval}." + "{symbol}"
        self.subscribe(topic, callback, symbol)


class WebSocketTrading(_V5TradeWebSocketManager):
    def __init__(self, recv_window=0, referral_id="", **kwargs):
        super().__init__(recv_window, referral_id, **kwargs)

    def place_order(self, callback, **kwargs):
        operation = "order.create"
        self._send_order_operation(operation, callback, kwargs)

    def amend_order(self, callback, **kwargs):
        operation = "order.amend"
        self._send_order_operation(operation, callback, kwargs)

    def cancel_order(self, callback, **kwargs):
        operation = "order.cancel"
        self._send_order_operation(operation, callback, kwargs)

    def place_batch_order(self, callback, **kwargs):
        operation = "order.create-batch"
        self._send_order_operation(operation, callback, kwargs)

    def amend_batch_order(self, callback, **kwargs):
        operation = "order.amend-batch"
        self._send_order_operation(operation, callback, kwargs)

    def cancel_batch_order(self, callback, **kwargs):
        operation = "order.cancel-batch"
        self._send_order_operation(operation, callback, kwargs)
