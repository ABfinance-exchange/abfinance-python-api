from enum import Enum


class Account(str, Enum):
    GET_WALLET_BALANCE = "/v5/account/wallet-balance"
    GET_TRANSFERABLE_AMOUNT = "/v5/account/withdrawal"
    GET_BORROW_HISTORY = "/v5/account/borrow-history"
    GET_COLLATERAL_INFO = "/v5/account/collateral-info"
    SET_COLLATERAL_COIN = "/v5/account/set-collateral-switch"
    BATCH_SET_COLLATERAL_COIN = "/v5/account/set-collateral-switch-batch"
    GET_FEE_RATE = "/v5/account/fee-rate"
    GET_ACCOUNT_INFO = "/v5/account/info"
    GET_TRANSACTION_LOG = "/v5/account/transaction-log"
    GET_MMP_STATE = "/v5/account/mmp-state"
    GET_INSTRUMENTS_INFO = "/v5/account/instruments-info"
    QUERY_DCP_INFO = "/v5/account/query-dcp-info"
    GET_SMP_GROUP = "/v5/account/smp-group"
    SET_LIMIT_PRICE_ACTION = "/v5/account/set-limit-px-action"

    def __str__(self) -> str:
        return self.value
