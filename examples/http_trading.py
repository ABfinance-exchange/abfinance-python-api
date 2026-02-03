"""
HTTP Trading Example

Demonstrates trading operations via HTTP API:
- Place order
- Query orders
- Amend order
- Cancel order
- Batch operations
"""

from abfinance_api.unified_trading import HTTP

session = HTTP(
    testnet=True,
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
)

# =============================================================================
# Place a limit order
# =============================================================================

print("=== Place Limit Order ===")
order_result = session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.001",
    price="50000",
)
print(order_result)

order_id = order_result.get("result", {}).get("orderId")
print(f"Order ID: {order_id}")

# =============================================================================
# Query open orders
# =============================================================================

print("\n=== Open Orders ===")
print(session.get_open_orders(category="spot", symbol="BTCUSDT"))

# =============================================================================
# Get order history
# =============================================================================

print("\n=== Order History ===")
print(session.get_order_history(category="spot", symbol="BTCUSDT", limit=5))

# =============================================================================
# Amend order (modify price/qty)
# =============================================================================

if order_id:
    print("\n=== Amend Order ===")
    print(session.amend_order(
        category="spot",
        symbol="BTCUSDT",
        orderId=order_id,
        price="49000",
    ))

# =============================================================================
# Cancel order
# =============================================================================

if order_id:
    print("\n=== Cancel Order ===")
    print(session.cancel_order(
        category="spot",
        symbol="BTCUSDT",
        orderId=order_id,
    ))

# =============================================================================
# Cancel all orders
# =============================================================================

print("\n=== Cancel All Orders ===")
print(session.cancel_all_orders(category="spot", symbol="BTCUSDT"))

# =============================================================================
# Batch place orders
# =============================================================================

print("\n=== Batch Place Orders ===")
batch_request = [
    {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Limit",
        "qty": "0.001",
        "price": "48000",
    },
    {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Limit",
        "qty": "0.001",
        "price": "47000",
    },
]
print(session.place_batch_order(category="spot", request=batch_request))

# =============================================================================
# Get executions (trade history)
# =============================================================================

print("\n=== Executions ===")
print(session.get_executions(category="spot", symbol="BTCUSDT", limit=5))
