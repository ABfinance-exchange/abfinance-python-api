import logging
from dataclasses import dataclass
from abfinance_api.exceptions import (
    InvalidChannelTypeError,
    TopicMismatchError,
    UnauthorizedExceptionError,
)
from ._v5_market import MarketHTTP
from ._v5_trade import TradeHTTP
from ._v5_account import AccountHTTP
from ._v5_asset import AssetHTTP
from ._v5_user import UserHTTP
from ._v5_earn import EarnHTTP
from ._websocket_stream import _V5WebSocketManager
from ._websocket_trading import _V5TradeWebSocketManager


logger = logging.getLogger(__name__)

WSS_NAME = "Unified V5"
PRIVATE_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.{TLD}/v5/private"
PUBLIC_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.com/v5/public/{CHANNEL_TYPE}"
AVAILABLE_CHANNEL_TYPES = [
    "inverse",
    "linear",
    "spot",
    "option",
    "misc/status",
    "private",
]


@dataclass
class HTTP(
    MarketHTTP,
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    UserHTTP,
    EarnHTTP,
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

    def _validate_system_topic(self):
        if not self.WS_URL.endswith("misc/status"):
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

    def position_stream(self, callback):
        """Subscribe to the position stream to see changes to your position data in real-time.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "position"
        self.subscribe(topic, callback)

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

    def fast_execution_stream(self, callback, categorised_topic=""):
        """Fast execution stream significantly reduces data latency compared
        original "execution" stream. However, it pushes limited execution type
        of trades, and fewer data fields.
        Use categorised_topic as a filter for a certain `category`. See docs.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "execution.fast"
        if categorised_topic:
            topic += "." + categorised_topic
        self.subscribe(topic, callback, categorised_topic)

    def wallet_stream(self, callback):
        """Subscribe to the wallet stream to see changes to your wallet in real-time.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "wallet"
        self.subscribe(topic, callback)

    def greek_stream(self, callback):
        """Subscribe to the greeks stream to see changes to your greeks data in real-time. option only.

        Push frequency: real-time

        """
        self._validate_private_topic()
        topic = "greeks"
        self.subscribe(topic, callback)

    # Public topics

    def orderbook_stream(self, depth: int, symbol: (str, list), callback):
        """Subscribe to the orderbook stream. Supports different depths.

        Linear & inverse:
        Level 1 data, push frequency: 10ms
        Level 50 data, push frequency: 20ms
        Level 200 data, push frequency: 100ms
        Level 500 data, push frequency: 100ms

        Spot:
        Level 1 data, push frequency: 10ms
        Level 50 data, push frequency: 20ms

        Option:
        Level 25 data, push frequency: 20ms
        Level 100 data, push frequency: 100ms

        Required args:
            symbol (string/list): Symbol name(s)
            depth (int): Orderbook depth

        """
        self._validate_public_topic()
        topic = f"orderbook.{depth}." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def rpi_orderbook_stream(self, symbol: (str, list), callback):
        """Subscribe to the orderbook stream. Supports different depths.

        Spot, Perpetual & Futures:
        Level 50 data, push frequency: 100ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = f"orderbook.rpi." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def trade_stream(self, symbol: (str, list), callback):
        """
        Subscribe to the recent trades stream.
        After subscription, you will be pushed trade messages in real-time.

        Push frequency: real-time

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = f"publicTrade." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def ticker_stream(self, symbol: (str, list), callback):
        """Subscribe to the ticker stream.

        Push frequency: 100ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = "tickers.{symbol}"
        self.subscribe(topic, callback, symbol)

    def kline_stream(self, interval: int, symbol: (str, list), callback):
        """Subscribe to the klines stream.

        Push frequency: 1-60s

        Required args:
            symbol (string/list): Symbol name(s)
            interval (int): Kline interval

        """
        self._validate_public_topic()
        topic = f"kline.{interval}." + "{symbol}"
        self.subscribe(topic, callback, symbol)

    def liquidation_stream(self, symbol: (str, list), callback):
        """
        Pushes at most one order per second per symbol.
        As such, this feed does not push all liquidations that occur.

        Push frequency: 1s

        Required args:
            symbol (string/list): Symbol name(s)

        """
        logger.warning("liquidation_stream() is deprecated. Please use "
                       "all_liquidation_stream().")
        self._validate_public_topic()
        topic = "liquidation.{symbol}"
        self.subscribe(topic, callback, symbol)

    def all_liquidation_stream(self, symbol: (str, list), callback):
        """

        Push frequency: 500ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = "allLiquidation.{symbol}"
        self.subscribe(topic, callback, symbol)

    def insurance_pool_stream(self, contract_group: (str, list), callback):
        """Subscribe to the insurance pool stream.

        Push frequency: 1s

        Required args:
            contract_group (string/list): A contract group, eg "USDT" for
                USDT-margined contracts

        """
        self._validate_public_topic()
        symbol = contract_group
        topic = "insurance.{symbol}"
        self.subscribe(topic, callback, symbol)

    def price_limit_stream(self, symbol: str, callback):
        """Subscribe to the order price limit stream.

        Push frequency: 300ms

        Required args:
            symbol (string/list): Symbol name(s)

        """
        self._validate_public_topic()
        topic = "priceLimit.{symbol}"
        self.subscribe(topic, callback, symbol)

    # System status topics
    
    def system_status_stream(self, callback):
        """Subscribe to the system's status for when there's platform
        maintenance or a service incident.

        Push frequency: N/A

        """
        self._validate_system_topic()
        topic = "system.status"
        self.subscribe(topic, callback)


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
